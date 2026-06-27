import re

with open("index.php", "r") as f:
    content = f.read()

# Replace the grid
old_grid_pattern = re.compile(r'<!-- Masonry / Grid -->(.*?)<!-- Hidden Data -->', re.DOTALL)
new_grid = """<!-- Masonry / Grid -->
        <main class="b-grid">
            
            <!-- Highlight: Bio & One Pager -->
            <button class="b-block open-window bg-dark span-2x2" data-target="rh-bio-onepager">
                <svg class="tangram text-light" viewBox="0 0 100 100"><polygon points="0,100 50,0 100,100" fill="currentColor"/></svg>
                <div class="center-content"><h2 class="text-light">BIO &<br>ONE PAGER</h2></div>
                <div class="corner-label text-light">[01]<br>Profile</div>
            </button>
            
            <!-- Highlight: Presskit & Tech Rider -->
            <button class="b-block open-window bg-dark span-2x2" data-target="rh-presskit-techrider">
                <svg class="tangram text-light" viewBox="0 0 100 100"><polygon points="0,0 100,0 0,100" fill="currentColor"/></svg>
                <div class="center-content"><h2 class="text-light">PRESSKIT &<br>TECH RIDER</h2></div>
                <div class="corner-label text-light">[02]<br>Documents</div>
            </button>

            <!-- Highlight: Pictures -->
            <a href="https://www.dropbox.com/scl/fo/z52mw2c0a2gqj1pzkdwok/AJcLjA6iIz3Y0XCN04XBPLs?rlkey=m6awcj9g5qyhq3ydro084ectv&e=1&st=ss6tolmi&dl=0" target="_blank" class="b-block bg-dark span-2x2">
                <svg class="tangram text-light" viewBox="0 0 100 100"><polygon points="0,50 50,0 100,50 50,100" fill="currentColor"/></svg>
                <div class="center-content"><h2 class="text-light">PICTURES</h2></div>
                <div class="corner-label text-light">[03]<br>Photos</div>
            </a>

            <!-- Highlight: Logo -->
            <a href="https://www.dropbox.com/scl/fo/dxdf0orvxfdfao6v77trm/h?rlkey=8czc2sim075ig6313ndkngh9q&st=qkko5vfp&dl=0" target="_blank" class="b-block bg-dark span-2x2">
                <svg class="tangram text-light" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="currentColor"/></svg>
                <div class="center-content"><h2 class="text-light">LOGO</h2></div>
                <div class="corner-label text-light">[04]<br>Branding</div>
            </a>

            <!-- Block 05: Asset Repo (Cleaned up) -->
            <div class="b-block" style="align-items: flex-start; justify-content: space-between; text-align: left; cursor: default;">
                <svg class="tangram" viewBox="0 0 100 100" style="width: 300px; height: 300px; opacity: 0.03;"><polygon points="50,0 100,25 100,75 50,100 0,75 0,25" fill="currentColor"/></svg>
                
                <div class="center-content" style="width: 100%; display: flex; flex-direction: column; padding-bottom: 3rem;">
                    <h2 style="margin-bottom: 1.5rem; text-align: left;">ASSET<br>REPO</h2>
                    
                    <a href="https://www.dropbox.com/scl/fo/zwlmswazqe6ondrr3xlt9/h?rlkey=cdy4xowjmtwhw7dvvlgsezjgh&st=1n8qfjrp&dl=0" target="_blank" class="rh-row" style="padding: 0.5rem 0; border-bottom: 1px solid rgba(17,17,17,0.1);"><span class="rh-label" style="font-size: 1rem;">Show Videos</span><span class="rh-val" style="font-size: 0.8rem;">Dropbox ↗</span></a>
                    <a href="https://www.dropbox.com/scl/fo/3rrm3w8qax92fh7jehpu2/h?rlkey=4h57u39h923ukoinyejybsob4&st=2aovcnyv&dl=0" target="_blank" class="rh-row" style="padding: 0.5rem 0; border-bottom: none;"><span class="rh-label" style="font-size: 1rem;">Live LED Visuals</span><span class="rh-val" style="font-size: 0.8rem;">Dropbox ↗</span></a>
                </div>
                
                <div class="corner-label">[05]<br>Videos</div>
            </div>

            <!-- Block 06: Directory -->
            <button class="b-block open-window" data-target="rh-contacts">
                <svg class="tangram" viewBox="0 0 100 100"><rect x="35" y="0" width="30" height="100" fill="currentColor"/><rect x="0" y="35" width="100" height="30" fill="currentColor"/></svg>
                <div class="center-content"><h2>DIRECTORY</h2></div>
                <div class="corner-label">[06]<br>Contacts</div>
            </button>

            <!-- Block 07: Social Links -->
            <button class="b-block open-window" data-target="rh-socials">
                <svg class="tangram" viewBox="0 0 100 100"><polygon points="0,50 50,0 100,50 50,100" fill="currentColor"/></svg>
                <div class="center-content"><h2>SOCIAL LINKS</h2></div>
                <div class="corner-label">[07]<br>Network</div>
            </button>

            <!-- Block 08: Music -->
            <button class="b-block open-window" data-target="rh-stores">
                <svg class="tangram" viewBox="0 0 100 100"><polygon points="0,0 50,50 0,100" fill="currentColor"/><polygon points="100,0 50,50 100,100" fill="currentColor"/></svg>
                <div class="center-content"><h2>MUSIC</h2></div>
                <div class="corner-label">[08]<br>Streaming</div>
            </button>

            <!-- Block 09: Press Links -->
            <button class="b-block open-window" data-target="rh-press">
                <svg class="tangram" viewBox="0 0 100 100"><rect x="10" y="10" width="35" height="35" fill="currentColor"/><rect x="55" y="10" width="35" height="35" fill="currentColor"/><rect x="10" y="55" width="35" height="35" fill="currentColor"/><rect x="55" y="55" width="35" height="35" fill="currentColor"/></svg>
                <div class="center-content"><h2>PRESS LINKS</h2></div>
                <div class="corner-label">[09]<br>Articles</div>
            </button>

            <!-- Block 10: Kratex TV -->
            <a href="http://tv.kratex.in" target="_blank" class="b-block">
                <svg class="tangram" viewBox="0 0 100 100"><rect x="10" y="20" width="80" height="60" fill="currentColor"/><polygon points="40,20 50,0 60,20" fill="currentColor"/></svg>
                <div class="center-content"><h2>KRATEX TV</h2></div>
                <div class="sub-desc">Exclusive sets</div>
                <div class="corner-label">[10]<br>Video</div>
            </a>

            <!-- Block 11: Shop -->
            <a href="http://shop.kratex.in" target="_blank" class="b-block">
                <svg class="tangram" viewBox="0 0 100 100"><polygon points="20,20 80,20 100,100 0,100" fill="currentColor"/><rect x="40" y="0" width="20" height="20" fill="currentColor"/></svg>
                <div class="center-content"><h2>SHOP</h2></div>
                <div class="sub-desc">Merchandise</div>
                <div class="corner-label">[11]<br>Store</div>
            </a>

            <!-- Block 12: Shows -->
            <a href="http://shows.kratex.in" target="_blank" class="b-block">
                <svg class="tangram" viewBox="0 0 100 100"><rect x="0" y="30" width="100" height="40" fill="currentColor"/><circle cx="0" cy="50" r="15" fill="currentColor"/><circle cx="100" cy="50" r="15" fill="currentColor"/></svg>
                <div class="center-content"><h2>SHOWS</h2></div>
                <div class="sub-desc">Tour dates</div>
                <div class="corner-label">[12]<br>Tour</div>
            </a>

        </main>
    </div>

    <!-- Hidden Data -->"""

content = old_grid_pattern.sub(new_grid, content)

# Replace the modals
old_modals_pattern = re.compile(r'<!-- RABBIT HOLES \(Full Screen Overlays\) -->(.*?)<!-- Toast Notification -->', re.DOTALL)
new_modals = """<!-- RABBIT HOLES (Full Screen Overlays) -->
    
    <!-- RH: Bio & One Pager -->
    <div class="rabbit-hole" id="rh-bio-onepager">
        <div class="rh-header">
            <h2 class="rh-title">BIO & ONE PAGER</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content text-body" id="target-bio-onepager"></div>
        <div class="rh-footer">
            <button class="os-btn copy-btn" data-target="target-bio-onepager">COPY TEXT</button>
        </div>
    </div>

    <!-- RH: Presskit & Tech Rider -->
    <div class="rabbit-hole" id="rh-presskit-techrider">
        <div class="rh-header">
            <h2 class="rh-title">PRESSKIT & TECH RIDER</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content rh-presskit-layout">
            <div class="rh-presskit-info">
                <div>
                    <h3>Kratex Official Assets</h3>
                    <p>The ultimate collection of assets for press, bookings, and promotional coverage.</p>
                    
                    <ul class="presskit-features">
                        <li><strong>Presskit:</strong> Comprehensive profile & milestones</li>
                        <li><strong>Tech Rider:</strong> Sound, lights, & staging requirements</li>
                    </ul>
                </div>
            </div>
            
            <div class="rh-presskit-viewer" style="display: flex; flex-direction: column; gap: 1rem; justify-content: center; align-items: center; background: transparent; border: none; box-shadow: none;">
                <a href="assets/pdf/kratex_presskit_2026.pdf" target="_blank" class="os-btn" style="width: 100%; max-width: 400px; padding: 2rem;">VIEW PRESSKIT ↗</a>
                <a href="https://www.dropbox.com/scl/fi/u9ykxtk3gx8oid9esm5c4/Kratex-Tech-Hospitality-Rider.pdf?rlkey=9m1q8wjfsbqtqk0hf023q07tf&st=mpyh1he5&dl=0" target="_blank" class="os-btn" style="width: 100%; max-width: 400px; padding: 2rem;">VIEW TECH RIDER ↗</a>
            </div>
        </div>
    </div>

    <!-- RH: Contacts -->
    <div class="rabbit-hole" id="rh-contacts">
        <div class="rh-header">
            <h2 class="rh-title">DIRECTORY</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content">
            <div class="rh-row">
                <span class="rh-label">MANAGEMENT: ROCK KACCHI</span>
                <span class="rh-val">+91 9834179271 ↗</span>
            </div>
            <a href="mailto:rock@worldofvibes.com" class="rh-row">
                <span class="rh-label">EMAIL MANAGER</span>
                <span class="rh-val">rock@worldofvibes.com ↗</span>
            </a>
            <a href="https://www.kratex.in" target="_blank" class="rh-row">
                <span class="rh-label">OFFICIAL WEBSITE</span>
                <span class="rh-val">www.kratex.in ↗</span>
            </a>
            <a href="mailto:contact@kratex.in" class="rh-row">
                <span class="rh-label">KRATEX CONTACT</span>
                <span class="rh-val">contact@kratex.in ↗</span>
            </a>
        </div>
    </div>

    <!-- RH: Socials -->
    <div class="rabbit-hole" id="rh-socials">
        <div class="rh-header">
            <h2 class="rh-title">SOCIAL LINKS</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content">
            <div class="rh-row">
                <a href="https://instagram.com/kratexmusic" target="_blank" class="rh-label">Instagram ↗</a>
                <button class="small-copy" data-copy="https://instagram.com/kratexmusic">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://x.com/kratexmusic" target="_blank" class="rh-label">X (Twitter) ↗</a>
                <button class="small-copy" data-copy="https://x.com/kratexmusic">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://facebook.com/kratexmusic" target="_blank" class="rh-label">Facebook ↗</a>
                <button class="small-copy" data-copy="https://facebook.com/kratexmusic">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://open.spotify.com/artist/3Gowc3dedLQgQAt4y0gPBo" target="_blank" class="rh-label">Spotify ↗</a>
                <button class="small-copy" data-copy="https://open.spotify.com/artist/3Gowc3dedLQgQAt4y0gPBo">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://www.youtube.com/@Kratexmusic" target="_blank" class="rh-label">YouTube ↗</a>
                <button class="small-copy" data-copy="https://www.youtube.com/@Kratexmusic">COPY</button>
            </div>
        </div>
    </div>

    <!-- RH: Stores -->
    <div class="rabbit-hole" id="rh-stores">
        <div class="rh-header">
            <h2 class="rh-title">MUSIC</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content">
            <div class="rh-row">
                <a href="https://open.spotify.com/artist/3Gowc3dedLQgQAt4y0gPBo" target="_blank" class="rh-label">Spotify ↗</a>
                <button class="small-copy" data-copy="https://open.spotify.com/artist/3Gowc3dedLQgQAt4y0gPBo">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://music.apple.com/nz/artist/kratex/1054012287" target="_blank" class="rh-label">Apple Music ↗</a>
                <button class="small-copy" data-copy="https://music.apple.com/nz/artist/kratex/1054012287">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://music.amazon.com/artists/B0185OP69C/kratex" target="_blank" class="rh-label">Amazon Music ↗</a>
                <button class="small-copy" data-copy="https://music.amazon.com/artists/B0185OP69C/kratex">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://kratex.bandcamp.com/" target="_blank" class="rh-label">Bandcamp ↗</a>
                <button class="small-copy" data-copy="https://kratex.bandcamp.com/">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://www.jiosaavn.com/artist/kratex-songs/lTbOhjmKg5M_" target="_blank" class="rh-label">JioSaavn ↗</a>
                <button class="small-copy" data-copy="https://www.jiosaavn.com/artist/kratex-songs/lTbOhjmKg5M_">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://gaana.com/artist/kratex" target="_blank" class="rh-label">Gaana ↗</a>
                <button class="small-copy" data-copy="https://gaana.com/artist/kratex">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://soundcloud.com/kratexmusic" target="_blank" class="rh-label">Soundcloud ↗</a>
                <button class="small-copy" data-copy="https://soundcloud.com/kratexmusic">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://www.beatport.com/artist/kratex/517636" target="_blank" class="rh-label">Beatport ↗</a>
                <button class="small-copy" data-copy="https://www.beatport.com/artist/kratex/517636">COPY</button>
            </div>
            <div class="rh-row">
                <a href="https://www.youtube.com/channel/UCgZsBbu8JHPdhMgPFubRnxQ" target="_blank" class="rh-label">YouTube ↗</a>
                <button class="small-copy" data-copy="https://www.youtube.com/channel/UCgZsBbu8JHPdhMgPFubRnxQ">COPY</button>
            </div>
        </div>
    </div>

    <!-- RH: Press Links -->
    <div class="rabbit-hole" id="rh-press">
        <div class="rh-header">
            <h2 class="rh-title">PRESS LINKS</h2>
            <button class="rh-close win-close">CLOSE [X]</button>
        </div>
        <div class="rh-content">
            <a href="https://rollingstoneindia.com/" target="_blank" class="rh-row"><span class="rh-label">Rolling Stone India</span><span class="rh-val">Read ↗</span></a>
            <a href="https://timesofindia.indiatimes.com/" target="_blank" class="rh-row"><span class="rh-label">The Times of India</span><span class="rh-val">Read ↗</span></a>
            <a href="https://indianexpress.com/" target="_blank" class="rh-row"><span class="rh-label">The Indian Express</span><span class="rh-val">Read ↗</span></a>
            <a href="https://www.theticketfairy.com/news/" target="_blank" class="rh-row"><span class="rh-label">TFword</span><span class="rh-val">Read ↗</span></a>
            <a href="https://www.youtube.com/" target="_blank" class="rh-row"><span class="rh-label">Beyond Bar & Bench</span><span class="rh-val">Watch ↗</span></a>
            <a href="https://theoutsiders.in/" target="_blank" class="rh-row"><span class="rh-label">The Outsiders</span><span class="rh-val">Read ↗</span></a>
        </div>
    </div>

    <!-- Toast Notification -->"""

content = old_modals_pattern.sub(new_modals, content)

# Update the JS part
old_js_pattern = re.compile(r"document\.getElementById\('target-brief'\)\.textContent = document\.getElementById\('brief-data'\)\.textContent;\s*document\.getElementById\('target-bio'\)\.textContent = document\.getElementById\('bio-data'\)\.textContent;")
new_js = """document.getElementById('target-bio-onepager').textContent = document.getElementById('brief-data').textContent + "\\n\\n---\\n\\n" + document.getElementById('bio-data').textContent;"""

content = old_js_pattern.sub(new_js, content)

with open("index.php", "w") as f:
    f.write(content)
