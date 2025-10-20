
// new code

const players = document.querySelectorAll('.audio-player');
        let currentAudio = null;
        let currentImage = null;

        const formatTime = (seconds) => {
            const minutes = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
        };

        players.forEach(player => {
            const playBtn = player.querySelector('.play-btn');
            const progress = player.querySelector('.progress');
            const progressBar = player.querySelector('.progress-bar');
            const currentTimeEl = player.querySelector('.current-time');
            const durationEl = player.querySelector('.duration');
            const volumeSlider = player.querySelector('.volume-slider');
            const speedSelect = player.querySelector('.speed-select');
            const songCard = player.closest('.song');
            const albumArt = songCard.querySelector('.album-art');
            const audio = new Audio(player.dataset.src);

            // Load duration
            audio.addEventListener('loadedmetadata', () => {
                durationEl.textContent = formatTime(audio.duration);
            });

            // Play/Pause toggle
            playBtn.addEventListener('click', () => {
                // Pause others
                if (currentAudio && currentAudio !== audio) {
                    currentAudio.pause();
                    document.querySelectorAll('.play-btn').forEach(btn => btn.textContent = '▶️');
                    if (currentImage) currentImage.classList.remove('rotate');
                }

                if (audio.paused) {
                    audio.play();
                    playBtn.textContent = '⏸️';
                    albumArt.classList.add('rotate');
                    currentAudio = audio;
                    currentImage = albumArt;
                } else {
                    audio.pause();
                    playBtn.textContent = '▶️';
                    albumArt.classList.remove('rotate');
                }
            });

            // Update progress and time
            audio.addEventListener('timeupdate', () => {
                const percent = (audio.currentTime / audio.duration) * 100;
                progressBar.style.width = `${percent}%`;
                currentTimeEl.textContent = formatTime(audio.currentTime);
            });

            // Seek on click
            progress.addEventListener('click', (e) => {
                const rect = progress.getBoundingClientRect();
                const clickX = e.clientX - rect.left;
                const width = rect.width;
                const seekTime = (clickX / width) * audio.duration;
                audio.currentTime = seekTime;
            });

            // Volume control
            volumeSlider.addEventListener('input', () => {
                audio.volume = volumeSlider.value;
            });

            // Speed control
            speedSelect.addEventListener('change', () => {
                audio.playbackRate = parseFloat(speedSelect.value);
            });

            // Reset on end
            audio.addEventListener('ended', () => {
                playBtn.textContent = '▶️';
                progressBar.style.width = '0%';
                currentTimeEl.textContent = '0:00';
                albumArt.classList.remove('rotate');
            });
        });