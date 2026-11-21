## This script defines the attributes for Society6 images.
## This includes detailed definitions and guidelines for each attribute category.
## It provides inclusions and exclusions for each attribute to ensure clarity in tagging.


attributes = ['subject_def','medium_def','pattern_def','style_def','color_def','Keywords_def']


subject_def = {"""Based on Subject Attribute Guide, please select the suitable Subject values that have score of greater than 70 percent.\n
                ────────────────────────────────────────────────────────────\n
                DETAILED Subject DEFINITIONS AND GUIDELINES\n
                ────────────────────────────────────────────────────────────\n

                1) Abstract\n
                    Definition: Art that is non-representational and does not depict recognizable subjects.\n
                    • Includes: Purely abstract forms, non-objective art, color field paintings, gestural abstraction, abstract shapes, abstract compositions, non-figurative art, conceptual abstract art.\n
                    • Excludes: Representational art, landscapes, cityscapes, portraits, still life, people, animals, botanical subjects, objects, places, events, cultural themes, political themes, occasions, issues and causes, or any artwork with recognizable subjects or themes.\n
               
                2) Animals\n
                    Definition: Depictions of wild animals in their natural habitats.\n
                    • Includes: African wildlife, jungle animals, forest animals, arctic animals, birds of prey (wild), marine wildlife, jungle animals, savanna animals, polar animals, woodland creatures, wild birds, wild mammals, wild reptiles, wild amphibians, wild insects.\n
                    • Excludes: Pet animals, farm animals, mythological animals, people, portraits, still life, landscapes, cityscapes, botanical subjects, objects, events, cultural themes, political themes, occasions, issues and causes.\n

                3) Architecture\n
                    Definition: Art depicting urban environments, cities, and architectural structures.\n
                    • Includes: Cityscapes (general), skylines, street scenes, architectural details, buildings (exterior views), urban environments, city life (architectural focus), urban landscapes, bridges (architectural focus), landmarks (architectural focus), interiors of buildings (architectural focus).\n
                    • Excludes: Landscapes (natural scenes), portraits, still life, people, animals, botanical subjects, objects, events, cultural themes, political themes, occasions, issues and causes (unless cityscape is symbolic of an issue, then use both 'Cityscapes & Architecture' and the specific issue category), abstract cityscapes (unless architecture is the basis of abstraction).\n
           
                4) Astrology\n
                    Definition: Art that represents or is inspired by celestial influences, zodiac signs, planetary movements, and astrological symbolism.\n
                    • Includes: Zodiac signs, horoscopes, planetary alignments, star charts, constellations, astrological symbols, birth charts, celestial elements, cosmic energy, tarot-inspired astrology, mysticism, and spiritual astrology.\n
                    • Excludes: General astronomy, scientific depictions of space, physics-based celestial studies, unrelated spiritual or mystical themes, and non-astrology-based fortune-telling.\n

                5) Cocktails\n
                    Definition: Art depicting cocktails, drinks, and beverages.\n
                    • Includes: Cocktail illustrations, drink recipes, cocktail photography, bar scenes, mixology art, beverage arrangements, cocktail garnishes, drink culture.\n
                    • Excludes: Food & drink still life (unless focusing on cocktails), floral still life, landscapes, cityscapes, portraits, people, animals, botanical subjects, objects, events, cultural themes, political themes, occasions, issues and causes.\n
                
                6) Desert\n
                    Definition: Arid landscapes with sand dunes, cacti, etc. Combine with Western (Theme) if it’s a cowboy scene, etc.\n
                    • Includes: Desert vistas, cacti, rock formations, oases, desert wildlife.\n
                    • Excludes: Non-arid landscapes, tropical or forest environments, ocean scenes, urban settings, and abstract art without recognizable desert elements.\n

                7) Flowers\n
                    Definition: Detailed close-up depictions of individual flowers.\n
                    • Includes: Single flower portraits, macro flower photography, detailed flower illustrations, flower anatomy studies (artistic), blossoms, petals, stamens, pistils, floral details, isolated flowers.\n
                    • Excludes: Floral patterns, flower arrangements (unless focusing on *individual* flower detail), landscapes, cityscapes, portraits, still life (unless flower is the *sole* focus of still life), people, animals, objects, events, cultural themes, political themes, occasions, issues and causes.\n

                8) Food\n
                    Definition: Still life arrangements featuring food and beverages.\n
                    • Includes: Fruit still life, vegetable still life, wine still life, coffee still life, breakfast still life, dessert still life, culinary still life, food arrangements, drink compositions, meals depicted as still life.\n
                    • Excludes: Floral still life, object still life, landscapes, cityscapes, portraits, people, animals, botanical subjects, events, cultural themes, political themes, occasions, issues and causes.\n

                9) Forest\n
                    Definition: Landscapes specifically featuring forests or woods.\n
                    • Includes: Dense forests, woodland scenes, forest paths, trees in forest, jungle landscapes (if focused on forest aspect), groves, wooded areas, rainforests, temperate forests, boreal forests.\n
                    • Excludes: Mountainscapes, seascapes, field/farmland scenes, cityscapes, interiors, portraits, still life, people, animals, botanical subjects, abstract forests (unless forests are the basis of abstraction), objects, events, cultural themes, political themes, occasions, issues and causes.\n

                10) Funny\n
                    Definition: Intended to amuse or entertain (humor, wit, comedy).nOften overlaps with “Kids” or “Animals” if done in a humorous style.\n
                    • Includes: Cartoons, caricatures, visual puns, comedic illustrations, exaggerated expressions, parody.\n
                    • Excludes: Serious/dramatic themes, purely abstract art with no comedic intent.\n
               
                11) Inspirational\n
                    Definition: Uplifting, Success, motivational, Achievement, Winning or encouraging. Often text-based (e.g., quotes) or symbolic imagery of success and perseverance.\n
                    • Includes: Motivational quotes, positive messages, scenes of triumph/resilience, personal empowerment, hope.\n
                    • Excludes: Negative or pessimistic themes, purely abstract with no uplifting text/message.\n

                12) Kids\n
                    Definition: Child-friendly or designed for children’s spaces. Can overlap with “Funny,” “Animals,” etc associated with children.\n
                    • Includes: Nursery themes, fairy tale illustrations, cartoon animals, bright or whimsical style.\n
                    • Excludes: Dark, violent, or overly mature content, realistic adult scenes.\n
               
                13) Landscape\n
                    Definition: Art depicting geographical locations, natural scenes, and environments.\n
                    • Includes: Landscapes (general), field/farmland scenes, riverscapes, tundra landscapes, arctic landscapes, gardens (landscape view), parks, geographical maps (artistic representation), nature scenes, outdoor environments.\n
                    • Excludes: Cityscapes, interiors, portraits, mountains, oceans, forests, tropical regions, still life, people, animals, botanical close-ups, abstract landscapes (use 'Abstract - Landscape' if primarily abstract), objects, events, cultural themes, political themes, occasions, issues and causes (unless location is directly symbolic of the issue, then use both 'Places & Landscapes' and the specific issue category).\n

                14) LGBTQ\n
                    Definition: Reflects LGBTQ+ identities, culture, pride, activism, or history. If the rainbow is specifically a Pride symbol, tag here rather than “Rainbows” in Subject.\n
                    • Includes: Pride flags, queer relationships, drag culture, famous LGBTQ+ figures or events.\n
                    • Excludes:Heteronormative romance with no LGBTQ+ context, general art with no reference to sexual orientation/gender identity.\n

                15) Lines\n
                    Definition: Pattern emphasizing line work as the primary element (contour, minimal line). Often pairs with “Abstract” or “Shapes” if it’s strongly linear.\n
                    • Includes: Continuous line drawings, geometric line patterns, minimalist outlines, optical illusions with lines.\n
                    • Excludes: Shaded realism, paintings where color fields/shapes dominate more than line.\n
  
                16) Mountains\n
                    Definition:Landscapes specifically featuring mountains.\n
                    • Includes: Mountain ranges, snow-capped mountains, mountain valleys, mountain peaks, alpine landscapes, foothills, rocky terrains, mountain vistas.\n
                    • Excludes: Seascapes, forest scenes, field/farmland scenes, cityscapes, interiors, portraits, still life, people, animals, botanical subjects, abstract landscapes (unless mountains are the basis of abstraction), objects, events, cultural themes, political themes, occasions, issues and causes.\n

                17) Music\n
                    Definition: Art featuring musical elements: instruments, notes, performers, or music culture. If it’s people playing music, you might multi-tag with People + Music.\n
                    • Includes: Guitars, pianos, sheet music, concerts, album-cover-inspired images.\n
                    • Excludes: Non-musical entertainment, abstract shapes with no music references.\n

                18) Nature\n
                    Definition: Generic label for natural environments or elements if no single subcategory (like mountains/ocean) dominates. If one specific nature subcategory is clearly the focus, use that (e.g., Forest, Ocean, etc.).\n
                    • Includes: Mixed natural scenes, general “outdoors” with multiple features.\n
                    • Excludes: Pure cityscapes, industrial settings, purely abstract.\n

                19) Ocean\n
                    Definition: Landscapes specifically featuring the sea or ocean.\n
                    • Includes: Ocean waves, beaches, coastlines, cliffs (coastal), harbors, seashores, seas, oceans, coastal views, marine environments, nautical scenes.\n
                    • Excludes: Mountainscapes, forest scenes, field/farmland scenes, cityscapes, interiors, portraits, still life, people, animals, botanical subjects, abstract seascapes (unless seas are the basis of abstraction), objects, events, cultural themes, political themes, occasions, issues and causes.\n             

                20) Space\n
                    Definition: Art depicting space, space exploration, and celestial bodies.\n
                    • Includes: Planets, stars, galaxies, nebulae, astronauts, spaceships, telescopes, space stations, lunar landscapes, Martian landscapes,宇宙, interstellar travel, cosmic phenomena, astronomical events.\n
                    • Excludes: Anatomy, medical themes, other Science & Technology subcategories (unless combined), Abstract art, Places & Landscapes (unless space landscapes), Cityscapes & Architecture, Portraits, Still Life, People, Animals, Botanical Subjects, Objects, Events & Occasions, Cultural Themes, Political Themes & Movements, Issues & Causes.\n

                21) Plants\n
                    Definition: Art depicting plants, flowers, trees, and other flora.\n
                    • Includes: Botanical art (general), flower close-ups, plant studies, tree portraits, botanical illustrations, floral arrangements (botanical focus), gardens (botanical detail focus), trees (individual tree focus), leaves, foliage, fruits (botanical focus, use 'Still Life - Food & Drink' if food context is primary).\n
                    • Excludes: Landscapes (unless botanical elements are the *sole* focus of the landscape), cityscapes, portraits, still life (unless botanical elements are the *primary subject* of still life), people, animals, objects, events, cultural themes, political themes, occasions, issues and causes (unless botanical elements are symbolic of an issue, then use both 'Botanical' and the specific issue category), floral patterns (use 'Pattern - Floral' for patterns).\n

                22) Portraits\n
                    Definition: Portraits specifically of human subjects, individuals.\n
                    • Includes: Male portraits, female portraits, child portraits, elderly portraits, individual portraits, formal portraits, informal portraits, self-portraits, headshots, busts (portrait focus), full-body portraits, celebrity portraits.\n
                    • Excludes: Animal portraits, group portraits, crowd scenes, figurative art (general figure studies), still life, landscapes, cityscapes, animals, botanical subjects, objects, events, cultural themes, political themes, occasions, issues and causes.\n
           
                23) Rainbows\n
                    Definition: Atmospheric phenomenon featuring a rainbow arc in the sky. Since this is part of “Nature,” use it if a natural rainbow is the main subject.\n
                    • Includes: Natural rainbows after rain, rainbow arcs in landscapes, realistic rainbow imagery.\n
                    • Excludes: Merely colorful art with no distinct rainbow shape, Pride flags focusing on LGBTQ symbolism (see Theme: LGBTQ).\n

                24) Shapes\n
                    Definition: Patterns based on geometric shapes and lines. that depicts geometric shapes like triangle, circle, square, rectangle, semi-circle.\n
                    • Includes: Stripes, polka dots, chevron, herringbone, plaid/tartan, abstract geometric patterns, tessellations, argyle, camouflage, checkered/gingham, houndstooth, geometric shapes in repeating arrangements.\n
                    • Excludes: Floral patterns, botanical patterns, animal patterns, abstract patterns (unless geometric shapes are the basis), typographic patterns, motif-based patterns (unless geometric shapes are motifs).\n

                25) Sports\n 
                    Definition: Art depicting sports, games, outdoor activities, travel, and hobbies.\n
                    • Includes: Sports (general), specific sports (basketball, soccer, etc.), games (board games, video games, etc.), outdoor activities (hiking, camping, fishing, etc.), travel destinations, travel scenes, vacations, toys (artistic representation), hobbies (various hobbies depicted), leisure activities, recreational pursuits.\n
                    • Excludes: Abstract art, Places & Landscapes (unless landscape is *part* of the recreation, e.g., landscape painting *of* hikers), Cityscapes & Architecture, Portraits, Still Life, People (unless depicting people *engaged* in recreation), Animals, Botanical Subjects, Objects, Events & Occasions, Cultural Themes, Political Themes & Movements, Issues & Causes.\n

                26) Still Life\n
                    Definition: Still life arrangements featuring everyday or specific objects.\n
                    • Includes: Book still life, musical instrument still life, tools still life, vintage object still life, household object still life, collections of objects, personal belongings as still life, symbolic objects in still life.\n
                    • Excludes: Food & drink still life, floral still life, landscapes, cityscapes, portraits, people, animals, botanical subjects, events, cultural themes, political themes, occasions, issues and causes.\n
                             
                27) Travel\n
                    Definition: Evokes exploration, adventure, or destinations. You can also tag with “Architecture” (Subject) or “Nature” (Subject) if it’s about traveling in natural settings.\n
                    • Includes: Travel destinations (landmarks, scenery), travel scenes (airports, trains, etc.), landscapes (travel focus), adventure activities (hiking, climbing, kayaking, etc.), exploration themes, journeys, wanderlust, maps (travel/adventure focus), tourism themes. Famous landmarks (as a theme), travel posters, maps, transportation icons (planes, trains) in a wanderlust context.\n
                    • Excludes: Generic architecture or cityscapes not framed as “travel,” purely local scenes with no sense of exploration.\n

                28) Tropical\n
                    Definition: Art depicting featuring tropical regions, ambiance, etc.\n
                    • Includes: Hibiscus patterns, orchid patterns, bird of paradise patterns, plumeria patterns, tropical flower arrangements, patterns with exotic flowers as the primary motif.\n
                    • Excludes: Common garden flower patterns (rose, tulip, daisy), botanical leaf or tree patterns, geometric or abstract patterns.\n
             
                29) Western\n
                    Definition: Themes of the American Old West or frontier culture. Often pairs with “Desert” in the Subject dimension if the environment is southwestern.\n
                    • Includes: Cowboys, horses, outlaws, saloons, rustic desert scenes, Western film references.\n
                    • Excludes: Contemporary city settings, purely desert without cowboy/western iconography, other global cultures not referencing the Old West.\n

                30) Typography\n
                    Definition: Patterns created using letters, numbers, calligraphy, something written in textual pattern, or other typographic elements.\n
                    • Includes: Letter patterns, number patterns, text-based patterns, alphabet patterns, patterns formed by repeating words or phrases, patterns using fonts and typography as the primary visual element.\n
                    • Excludes: Geometric patterns, floral patterns, botanical patterns, animal patterns, abstract patterns, motif-based patterns (unless letters or numbers are used as motifs).\n"""}


medium_def = {"""Based on Medium Attribute Guide, please select the suitable Medium values that have score of greater than 70 percent.\n
                Please note that the Medium should be consistent accross similar type of art work treatment.\n
                ────────────────────────────────────────────────────────────\n
                DETAILED Medium DEFINITIONS AND GUIDELINES\n
                ────────────────────────────────────────────────────────────\n

                a) Painting\n
                    Description: Artworks created by applying paint or pigment (in traditional or digital form) in a manner that mimics brushes, paint textures, or painterly styles.\n
                    • Includes: Oil, acrylic, watercolor paintings (physical or digital). Digital artworks that replicate a brush-painted look.\n
                    • Excludes: Purely photographic works, purely line-based drawings, clean-edged vector graphics.\n

                b) Drawing\n
                    Description: Artworks that emphasize line work and hand-drawn elements, traditionally or digitally, usually focusing on contour lines, shading with pencils, pens, charcoal, etc.\n
                    • Includes: Pencil sketches, ink drawings, charcoal or marker drawings, digital sketches that visually resemble hand-drawn line art.\n
                    • Excludes: Paint-heavy images, photos, vector-based or heavily stylized conceptual illustrations that serve a narrative function (→ see Illustration). Shapes that are filled-in. Conceptual scene with figurative characters\n

                c) Photography\n
                    Description: Artworks primarily captured through a camera (digital or analog), retaining most characteristic elements of a photo, even if lightly retouched or color-corrected.\n
                    • Includes: Color and B&W photography, fine-art photography, images with moderate digital edits like filters or simple touch-ups.\n
                    • Excludes: Heavily manipulated photographic elements that result in composite scenes or collages (→ see Collage).\n

                d) Vector Art\n
                    Description: Artworks created using vector software with crisp, clean edges; often characterized by flat areas of color or simple gradients, clearly defined shapes, and scalability without loss of quality.\n
                    • Includes: Flat design illustrations, geometric logos/posters, stylized vector graphics.\n
                    • Excludes: Raster paintings, photographic images, purely drawn linework without vector shapes.\n

                e) Collage\n
                    Description: Artworks formed by assembling multiple distinct images or fragments, either physically or digitally, into a cohesive whole.\n
                    • Includes: Photomontages, layering various elements, cutouts, or scanned imagery into a single piece.\n
                    • Excludes: A single unaltered photo, a solitary painting, a solitary drawing, or a singular digital illustration.\n

                f) Typography\n
                    Description: Art in which the primary visual focus is arranged text or lettering. The letters themselves become the primary artistic element. Textual art, Calligraphy, artristic textual work.\n
                    • Includes: Calligraphy-based works, designs primarily featuring stylized or artistic text, lettering art prints.\n
                    • Excludes: Pieces where any text is minimal or secondary to a large illustration/graphic (→ possibly see Graphic Design or Illustration).\n

                g) Graphic Design\n
                    Description: Visually composed layouts often intended for commercial or communicative purposes, where systematic design principles (layout, branding elements, systematic color schemes) are prominent.\n
                    • Includes: Infographics, brand or advertising posters, brochures, magazine layouts, or digital designs that prioritize structured visual communication.\n
                    • Excludes: Fine art painting, purely narrative or decorative illustrations, artworks focusing on text as the main art form (→ see Typography).\n

                h) Illustration\n
                    Description: Artworks created to depict or explain a story, subject, or concept—often figurative or representational, stylized to convey a specific narrative or idea.\n
                    • Includes: Editorial illustrations, storybook art, conceptual imagery, character and scene illustrations that visually represent an idea or story.\n
                    • Excludes: Pure line-based sketches or drawings (→ Drawing), logically structured commercial designs (→ Graphic Design), or photo manipulations (→ Collage).\n

                i) None\n
                    Description: Use only if the artwork clearly defies standard classification in all above categories.\n
                    • Example: Entirely abstract digital texture or generative art that does not exhibit clear traits of painting, drawing, photography, collage, etc.\n

                    ────────────────────────────────────────────────────────────\n
                    HANDLING AMBIGUITY AND EDGE CASES\n
                    ────────────────────────────────────────────────────────────\n

                    Dominance Rule:\n
                    If multiple traits appear, choose the category that visually or conceptually dominates. For instance, if a photo is heavily overlaid with multiple composited elements from other sources, Collage dominates over Photography.\n

                    Artist Intent Rule:\n
                    Consider why the piece was created and how it conveys meaning.\n
                    • Narrative enhancement → Illustration.\n
                    • Straightforward, primarily photo → Photography.\n
                    • Heavily composited or assembled → Collage.\n
                    • Clear brand or commercial style layout → Graphic Design.\n
                    • Stylized or realistic painting surfaces → Painting.\n
                    • Hand-drawn lines or sketches → Drawing.\n
                    • Main focus on stylized text → Typography.\n
                    • Crisp, flat, scalable shapes → Vector Art.\n

                    Examples:\n
                    • A vector-style poster with geometric shapes and text that looks like brand messaging → Graphic Design.\n
                    • A single photograph with light color correction → Photography.\n
                    • A digitally painted portrait showing brush-like effects → Painting.\n
                    • A pen-and-ink style line drawing → Drawing.\n
                    • Calligraphic text as the main focus → Typography.\n
                    • A storybook-like scene with stylized characters → Illustration.\n
                    • A digital collage of multiple photographic elements → Collage.\n
                    • An ambiguous or algorithmically generated abstract form that doesn’t fit any category → None (use rarely).\n

                    Final Answer Requirement:\n
                    Provide only the single best match from (a–i).\n"""}


pattern_def = {"""Based on Pattern Attribute Guide, please select the suitable Pattern values that have score of greater than 70 percent.\n
                ────────────────────────────────────────────────────────────\n
                DETAILED Pattern DEFINITIONS AND GUIDELINES\n
                ────────────────────────────────────────────────────────────\n
                1) Animal Print\n
                Definition: Clearly abstract patterns directly imitating animal skins, fur, or scales. Includes patterns derived from zebra stripes, leopard spots, snakeskin, giraffe pattern, tiger stripes, or other animal-printed textures such as claw marks.\n
                DO NOT classify: realistic animal depictions or illustrations of entire animals or birds.\n
                
                2) Botanical\n 
                Definition: Patterns highly dominated by detailed plant-based visual elements like leaves, branches, foliage, plants, palms, ferns, greenery. Flowers should not be main visual element.\n
                DO NOT classify: prominently floral-centered or animal-centered designs.\n
                
                3) Checks\n
                Definition: Patterns composed of repeated squares or rectangles forming consistent grids of two or more alternating colors created by intersecting horizontal and vertical lines (e.g. checkerboard, gingham).\n
                DO NOT classify: complex plaid/tartan designs.\n
                
                4) Chevron\n
                Definition: Patterns containing repetitive and regular zigzag lines with distinct V-shaped or inverted-V shapes.
                DO NOT classify: straight line (stripes) or irregular zigzag lines.
                
                5) Geometric\n
                Definition: Patterns clearly dominated by repetitive abstract geometric visual elements including lines (straight, wavy, angled), dots arranged symmetrically, circles, squares, polygons, triangles, diamonds, hexagons, or other orderly arranged geometric motifs.\n
                DO NOT classify: irregularly scattered dots without arrangement; organic, blurred ikat patterns or natural marble textures.
                
                6) Ikat\n
                Definition: Patterns visually resembling traditional ikat textiles with blurred edges, a woven-like texture, or dye-bleeding textiles appearance.\n
                DO NOT classify: clearly tie-dyed patterns or sharply geometric designs.\n
                
                7) Tie-Dyed\n
                Definition: Patterns displaying vibrant, organic-blended, dyed swirls, irregular spirals, bursts, resulting from tie-dye techniques.\n
                DO NOT classify: geometric symmetry, clearly marble stone patterns or ikat-like textiles.\n

                8) Floral\n
                Definition: Patterns strongly dominated by floral elements such as blossoms, petals, flowerheads. Flowers clearly form the more prominent visual design.\n
                DO NOT classify: patterns predominantly featuring non-floral botanical greenery or animals.\n

                9) Marble\n
                Definition: Patterns mimicking the natural visual appearance of marble stone, marbled beef steak, clearly featuring fluid, swirling veined textures.\n
                DO NOT classify: regular geometrical swirl patterns, natural tie-dye spirals, or random organic designs.\n

                10) Ombre\n
                Definition: Patterns showing color gradients transitioning gradually from one hue or shade to another without clearly defined borders like water on glass reflecting light\n
                DO NOT classify: designs with clear stripes, sharp color divisions, or abrupt changes.\n
                
                11) Dots\n
                Definition: Patterns primarily focused on irregularly or randomly scattered dots as their main visual motif. Dots are not neatly arranged in geometric repetitions or grids.\n
                DO NOT classify: well-organized or geometrically symmetrical dot arrangements.\n
                
                12) Plaid\n
                Definition: Complex pattern formed by multiple intersecting horizontal and vertical colored lines, creating visible overlapping bands and squares, like tartan designs.\n
                DO NOT classify: simple checks (like checkerboard/gingham) or purely geometric grids.\n
                
                13) Solid\n
                Definition: Patterns composed of a single flat uniform color with no patterns, no gradients, no theme, or no decorative variations.\n
                Solid will be a single flat color image only. For example a wallpaper of single plain, flat color without any texture.\n
                DO NOT classify: subtle variations, minimal gradients, or textures.\n
                
                14) Stripes\n
                Definition: Patterns clearly consisting of repeated parallel linear stripes (horizontal, vertical, or diagonal).\n
                DO NOT classify: zigzag chevron patterns, irregular wavy lines without clear repetition.\n
                
                15) Swirl\n
                Definition: Patterns predominantly featuring spiral shapes or swirling lines as the clearly decorative motif.\n
                DO NOT classify: marble textures or tie-dyed organic swirl patterns.\n
                
                16) None\n
                Definition: Art prints clearly depicting singular representational scenes, portraits, landscapes, still-life or realistic subjects explicitly without repetitive decorative motifs displayed.\n
                DO NOT classify: clear decorative motifs or repeated illustrated elements (even if realistic). Avoid classifying an image as 'None' if some of the other categories seem to apply.\n"""}


style_def = {"""Based on Style Attribute Guide, please select the suitable Style values that have score of greater than 70 percent.\n
                Please note that the Style should be consistent accross similar type of art work treatment.\n
                ────────────────────────────────────────────────────────────\n
                DETAILED Style DEFINITIONS AND GUIDELINES\n
                ────────────────────────────────────────────────────────────\n

                1)  Abstract\n
                    Definition: Non-representational or non-figurative art focusing on shapes, forms, colors, and textures.\n
                    • Includes: Paintings or prints with distorted shapes, splashes of color, geometric or fluid forms without recognizable subjects.\n
                    • Excludes: Artwork with clear, realistic depictions of people, animals, or objects as the main focus.\n
                    • Comments: If the artwork has no discernible subject matter, it is likely Abstract.\n

                2)  Antique\n
                    Definition: Art or prints that evoke a sense of relics from an older historical period (Pre-1900s or with an aged, classical look).\n
                    • Includes: Weathered, distressed imagery, old maps, vintage botanical illustrations, or reproductions of historical prints.\n
                    • Excludes: Simply “old-fashioned” modern pieces or newly made art with a slightly vintage feel (those might be “Vintage”).\n
                    • Comments: Focus is on genuine or convincingly reproduced historical aesthetics.\n

                3)  Anime\n
                    Definition: Art in the style of Japanese animation or manga, with specific stylized features such as large eyes, stylized hair, and expressive face.\n
                    • Includes: Art with clear anime/manga characters, typical anime linework, or known anime references.\n
                    • Excludes: Cartoon styles that are Western, Disney-like, or caricatures not fitting the anime conventions.\n
                    • Comments: If it looks specifically like Japanese manga/anime, it belongs here.\n

                4)  Art Deco\n
                    Definition: 1920s–1930s decorative style featuring bold geometric shapes, symmetry, and luxurious ornamentation.\n
                    • Includes: Stylized angular forms, repeated geometric patterns, gold accents, silhouettes reminiscent of the Roaring Twenties.\n
                    • Excludes: Merely geometric prints without the distinct 1920s–1930s flair.\n
                    • Comments: Look for glamour, geometric patterns, and a vintage 1920s vibe.\n

                5)  Art Nouveau\n
                    Definition: Late 19th–early 20th century style incorporating flowing, curving lines, floral motifs, and organic forms.\n
                    • Includes: Artwork with whiplash curves, decorative floral elements, elaborate borders, poster-style layouts akin to Alphonse Mucha.\n
                    • Excludes: Merely floral designs lacking the flowing lines and signature elongated shapes.\n
                    • Comments: Commonly features motifs of nature (flowers, vines), female figures in elegant, swirling forms.\n

                6)  Boho\n
                    Definition: Bohemian style often influenced by nature, hippie culture, earthy and eclectic vibes.\n
                    • Includes: Free-spirited, earthy color palettes, tribal or mandala patterns, dreamcatchers.\n
                    • Excludes: Strictly geometric or polished, glam aesthetics.\n
                    • Comments: Appeals to carefree, laid-back, eclectic sensibilities.\n

                7)  Cabin\n
                    Definition: Rustic, woodsy, outdoors-inspired. Evokes nature, lodges, and mountain or forest life.\n
                    • Includes: Wildlife motifs (bears, deer), plaid patterns, pine trees, rustic wood textures.\n
                    • Excludes: Modern, polished, or urban designs.\n
                    • Comments: If it looks like you’d see it in a mountain lodge or cabin décor, use this.\n

                8)  Cartoon\n
                    Definition: Western or non-Japanese cartoon style emphasizing exaggeration, playful characters, or comedic imagery.\n
                    • Includes: Comic strip styles, cartoon characters, Western animations (e.g., Looney Tunes style), caricatures.\n
                    • Excludes: Anime or manga aesthetics.\n
                    • Comments: If it’s playful, childlike, or typical Saturday-morning-cartoon style, select Cartoon.\n

                9)  Coastal\n
                    Definition: Beach- or ocean-inspired style focusing on seaside color palettes (e.g., blues, whites), marine life imagery.\n
                    • Includes: Seashell motifs, lighthouses, beach scenes, nautical stripes, driftwood.\n
                    • Excludes: Generic outdoor/nature scenes not obviously seaside.\n
                    • Comments: Overlaps with “Nautical” is possible; “Coastal” is more breezy, beach-house oriented.\n

                10) Contemporary\n
                    Definition: Current, trending style in art or interior design. Emphasizes clean lines, updated forms, can blend various influences.\n
                    • Includes: Modern, up-to-date abstract or figurative works aligned with recent design trends.\n
                    • Excludes: Clearly historic references, retro themes, or traditional artworks.\n
                    • Comments: Be careful not to confuse with “Modern,” which may refer to early 20th-century modernist movements.\n

                11) Eclectic\n
                    Definition: Mix-and-match aesthetic combining multiple styles, eras, or references.\n
                    • Includes: Artworks that merge various influences, layered or patchwork-like design.\n
                    • Excludes: Cohesive styles like purely Minimalism, purely Boho, etc.\n
                    • Comments: Use when the artwork clearly defies a single style and intentionally appears multi-styled.\n

                12) Farmhouse\n
                    Definition: Rustic, country-inspired aesthetic rooted in simplicity and rural charm.\n
                    • Includes: Distressed wood, farm animals, mason jars, vintage signage, pastoral motifs.\n
                    • Excludes: Sleek, modern lines or bright, pop-art colors.\n
                    • Comments: Typically has warm, cozy, rural vibes rather than purely “Cabin” or “Vintage”.\n

                13) Figurative\n
                    Definition: Representational artwork prominently featuring recognizable human or animal figures in a somewhat realistic manner.\n
                    • Includes: Portraits, realistic paintings or drawings of people, animals, or objects.\n
                    • Excludes: Abstract or purely decorative compositions.\n
                    • Comments: If the piece is realistically depicting humans or animals, put Figurative.\n

                14) Folk Art\n
                    Definition: Traditional, often handcrafted or naïve style associated with regional or cultural folk traditions.\n
                    • Includes: Simple, charming, possibly rustic motifs; decorative cultural patterns from specific ethnic crafts.\n
                    • Excludes: Contemporary, polished, academic realistic paintings.\n
                    • Comments: Focus is on folk culture influences, hand-crafted vibe, simpler form.\n

                15) Geometric\n
                    Definition: Art that features distinct shapes, lines, and patterns based purely or primarily on geometry.\n
                    • Includes: Repetitive triangles, circles, squares, polygonal designs, geometric abstractions.\n
                    • Excludes: Art Deco if it has that specific 1920s glam vibe; or purely abstract forms not focusing on geometry.\n
                    • Comments: If geometry is the main focus but not specifically Art Deco or Mid-Century, use “Geometric”.\n

                16) Glam\n
                    Definition: Luxurious, glitzy, or high-fashion style, often featuring metallics, sparkles, or bold, high-end design.\n
                    • Includes: Glitter, gold/silver metallic finishes, ornate looks, typically upscale or “Hollywood Regency” vibes.\n
                    • Excludes: Minimalist, rustic, vintage.\n
                    • Comments: Look for elements that convey luxury or star-studded fashion.\n

                17) Impressionism\n
                    Definition: 19th-century art style emphasizing light, brushstrokes, and capturing an “impression” of a scene rather than precise detail.\n
                    • Includes: Visible brushstrokes, soft edges, emphasis on lighting effects (e.g., Monet-like landscapes).\n
                    • Excludes: Sharp, photographic realism or modern digital illusions.\n
                    • Comments: Classic impressionist techniques or strongly reminiscent works.\n

                18) Mid-Century Modern\n
                    Definition: 1950s–1960s style featuring clean lines, organic curves, minimal ornamentation, and warm, earthy palettes.\n
                    • Includes: Vintage atomic patterns, retro furniture forms, abstract shapes typical of 50s design.\n
                    • Excludes: Straight-up Retro from other decades (e.g., 1980s neon).\n
                    • Comments: If it clearly matches the 1950–1960 design idioms, select Mid-Century Modern.\n

                19) Minimalism\n
                    Definition: Sleek, monochromatic or limited color palette, focusing on simplicity, deliberate use of space.\n
                    • Includes: Very few elements, negative space, simple lines, “less is more” aesthetics.\n
                    • Excludes: Busy patterns, excessive detail.\n
                    • Comments: If the artwork is extremely pared down, with few elements or colors, it’s likely Minimalism.\n

                20) Modern\n
                    Definition: Broad term for early-mid 20th-century modernist movements (e.g., modern art, modern design) emphasizing simplicity and functional forms.\n
                    • Includes: Bauhaus-inspired designs, early 20th-century avant-garde influences.\n
                    • Excludes: “Contemporary” which refers to more current styles, or “Mid-Century Modern” which is more specific.\n
                    • Comments: Use if it references the classical modern (1900s–1970s) tradition but is not specifically Mid-Century.\n

                21) Nautical\n
                    Definition: Related to ships, sailing, maritime themes.\n
                    • Includes: Anchors, ship wheels, rope motifs, navy-and-white stripes.\n
                    • Excludes: General sea/beach scenes that fit better under “Coastal”.\n
                    • Comments: Overlaps with “Coastal,” but go with “Nautical” if the theme is more about ships and seafaring.\n

                22) Pop Art\n
                    Definition: Mid- to late-20th century style using imagery from popular culture, bold outlines, bright colors, comic references.\n
                    • Includes: Roy Lichtenstein or Andy Warhol-inspired pieces, bold color blocks, repeated iconic images.\n
                    • Excludes: Random bright color usage without pop culture iconography.\n
                    • Comments: If it references mass media, product imagery, or comic-book styling with strong outlines, choose Pop Art.\n

                23) Psychedelic\n
                    Definition: Surreal, vibrant, mind-bending visuals often associated with 1960s counterculture.\n
                    • Includes: Swirling colors, fractal-like designs, hallucinatory motifs.\n
                    • Excludes: Merely bright palettes or abstract art without “trippy” or “hallucinatory” feel.\n
                    • Comments: Look for that ‘60s vintage rock-poster vibe or kaleidoscopic imagery.\n

                24) Retro\n
                    Definition: Typically referencing cultural aesthetics from a past era (1970s, 1980s, etc.) that is neither Mid-Century Modern nor purely Vintage.\n
                    • Includes: 70s patterns (bold florals, warm orange/brown), 80s neon gradients, old arcade poster styles.\n
                    • Excludes: 1950s (Mid-Century Modern) or very old (Antique), or broad “Vintage” that is older or more general.\n
                    • Comments: If referencing a specific decade “groovy 70s” or “neon 80s,” go with Retro.\n

                25) Scandavinian\n
                    Definition: Inspired by Nordic design: minimal, functional, nature-inspired, neutral or light color palettes.\n
                    • Includes: Clean lines, pale woods, soft textures, subtle patterns often with geometric or botanical touches.\n
                    • Excludes: Dark, opulent, or bright glam aesthetic.\n
                    • Comments: Often described as “clean, cozy, uncluttered, nature-honoring”.\n

                26) Surrealism\n
                    Definition: Artwork that depicts dreamlike, irrational, or fantastical scenes that defy realistic logic.\n
                    • Includes: Strange juxtapositions, floating objects, unusual transformations reminiscent of Dali, Magritte.\n
                    • Excludes: Merely abstract or figurative without uncanny or dreamlike elements.\n
                    • Comments: If it’s bizarre or dreamscape-like with hyperreal or imaginative scenarios, it’s likely Surrealism.\n

                27) Street Art\n
                    Definition: Artwork reflective of graffiti or urban mural culture, bold lettering, stencils, spray paint.\n
                    • Includes: Graffiti tags, large-scale mural styles, Banksy-like stenciled images.\n
                    • Excludes: Pop Art that references comics or commercial products but lacks street aesthetic.\n
                    • Comments: Often retains the look of spray paint, stencils, or urban grit.\n

                28) Traditional\n
                    Definition: Classic, academic, or historically conventional art styles (e.g., realistic oil paintings, classical still lifes, landscapes).\n
                    • Includes: Artwork reminiscent of renaissance, baroque, or classical painting techniques, or general realistic landscapes.\n
                    • Excludes: Impressionistic brushstrokes, modern or contemporary stylization.\n
                    • Comments: If it looks like typical academic, classical painting, use this. Not to be confused with “Antique” (which is specifically older or historical prints).\n

                29) Victorian\n
                    Definition: Ornate, decorative aesthetic typical of the Victorian era (mid-late 19th century).\n
                    • Includes: Highly decorative flourishes, romantic imagery, cameo silhouettes, elaborate frames.\n
                    • Excludes: Merely formal or classical painting lacking the Victorian stylistic flourishes.\n
                    • Comments: Look for the hallmark complexities, floral ornamentation, or lace-like details referencing 19th-century England.\n

                30) Vintage\n
                    Definition: Evokes mid-20th century nostalgia (or broad “retro” feel) but not specific enough for “Retro” or “Antique”.\n
                    • Includes: Old advertising posters, pin-up art, aged photographs from mid-20th century, “shabby-chic” older style.\n
                    • Excludes: Extremely old (Antique) or clearly decade-specific (Retro).\n
                    • Comments: General older (pre-1990s) vibe that isn’t strictly Antique or pinned to a certain decade.\n

                31) Watercolor\n
                    Definition: Art done in or emulating watercolor painting techniques — translucent layers, soft edges, fluid blending.\n
                    • Includes: Landscapes, florals, or figure studies with characteristic watery blending.\n
                    • Excludes: Acrylic or oil painting aesthetics; digital art that doesn’t mimic watercolor effect.\n
                    • Comments: If it has that distinct watery look with layers of translucent color, choose Watercolor.\n

                32) None\n
                    Definition: If the image does not fit any of the above categories or if classification confidence is too low.\n
                    • Includes: Everything that doesn’t strongly align with any defined style.\n
                    • Excludes: Use only when no other style is confidently applicable.\n
                    • Comments: Reserve for uncertain, ambiguous, or style-neutral image.\n"""}


color_def = {"""Based on Color Attribute Guide, please select the suitable Color values that have score of greater than 70 percent.\n
                Return the most dominant 2 colors in terms of coverage as top choices. So, at max just share 1st color with its score, then 2nd color with its score.\n
                If there exists more than 3 colors, return the dominant 2 colors, and then return the 3rd choice as Multicolor.\n
                In this manner no more than three results will appear for colors.\n
                ────────────────────────────────────────────────────────────\n
                DETAILED Color DEFINITIONS AND GUIDELINES\n
                ────────────────────────────────────────────────────────────\n
                a) Red\n
                Definition: Clearly predominantly red shades including crimson, burgundy, bright and deep reds. Crimson painting, Burgundy backdrop. Pink, orange hues or mixed evenly with other colors. Not pastel pink; must be definitively recognized as red.\n

                b) Orange\n
                Definition: Clearly orange-dominant color palette (bright, burnt orange, vivid true orange). Sunset orange, burnt orange art. Pale/soft peach shades, yellowish colors. Maintain clear distinction from peach tones.\n

                c) Peach\n
                Definition: Soft pastel-like pale orange-pink hues mainly dominant. Peach pastel prints, muted peach. Vivid orange, clear pink. Pastel-quality soft colors only.\n

                d) Yellow\n
                Definition: Clearly identifiable dominant yellow tones (bright, golden yellow, mustard). Sunflower yellow art, golden hues. Clearly greenish (avocado) or orange-dominant. Must clearly distinguish from avocado or orange shades.\n

                e) Avocado\n
                Definition: Yellowish-green muted shades matching ripe avocado colors. Olive-green artworks, avocado-toned prints. Bright pure greens, vivid yellows. Muted, yellowish-green hues only.\n

                f) Green\n
                Definition: Clearly recognizable green shades (emerald, forest, grass green). Grass-green paintings, forest landscapes. Avocado or teal shades. Clear mid-tone to dark greens only, no muted greyish or bluish shades.\n

                g) Sage\n
                Definition: Greyish-muted, desaturated green as the primary visual color. Pale, soft grey-green prints. Bright greens (forest, emerald), teal hues Only muted shades of greyish-green.\n

                h) Teal\n
                Definition: Clearly identifiable balanced blue-green hues (deep aqua, teal). Turquoise-teal paintings, ocean teal. Pure cyan arts or solid green hues. Clearly between blue-green spectrum balanced.\n

                i) Cyan\n
                Definition: Bright vivid clear blue-green hues (aquamarine, cyan dominant prints). Aquamarine, clear cyan art prints. Dark navy, teal balanced toward green-blue. Bright distinct highly saturated cyan hues only.\n

                j) Blue\n
                Definition: Medium clearly identifiable true-blue hues prominently shown. Royal blue, cobalt, sky blue prominently artwork. Navy, teal, purple tinted blues. Clear medium blue shades distinctly identifiable only.\n

                k) Navy\n
                Definition: Darker blue (navy, deep ocean shades) primary visual color. Indigo, navy prominently depicted artworks. Bright medium blues (sky blue, cobalt). Clear darker navy identified distinctly separate.\n

                l) Purple\n
                Definition: Clear violet, lavender or other purple hues strongly dominant. Lavender, clear purple prints. Pink or magenta clearly distinct. Purple identified hue strongly visible distinctly separate from magenta.\n

                m) Magenta\n
                Definition: Dominant rich pink-purple (magenta) shades distinctly identifiable. Bright, vivid magenta-colored artworks. Plain pink or clear-purple hues distinctly different. Vivid distinctly magenta shaded only.\n

                n) Pink\n
                Definition: Clearly identifiable pink shades (light pastel pink to brighter pink shades). Clearly identified pastel pink, true pink art Magenta (purple-pink) or peach (orange-pink). Avoid confusion clearly separate from magenta.\n

                o) Beige\n
                Definition: Predominantly neutral soft-warm cream, sand, beige shades. Warm neutral beige/sandy artworks. White strongly dominant or pastel other hues. Clearly neutral beige tones distinctly identified.\n

                p) Brown\n
                Definition: Clearly identified shades of medium to dark brown hues (chocolate, sepia). Sepia-tone prints, earthy-dark brown prints. Beige (lighter neutral) or distinctly orange/brown ambiguous shades Brown clearly identified darker prominent.\n

                q) Grey\n
                Definition: Dominantly neutral shades of grey (light to dark charcoal shades). Charcoal artworks, graphite-grey prints. Beige-toned neutral colors visibly warmer. Pure neutral grey shades only distinctly identifiable.\n

                r) Black\n
                Definition: Predominantly black monochromatic prints. Strongly dominant black artworks. Grey toned or clearly other-color dominant prints. Dominantly identified clear black hues.\n

                s) White\n
                Definition: Dominantly white and off-white shades. White monochrome, off-white dominant art. Beige warmer shades clearly separate. White clearly dominant tone distinctively recognizable.\n

                t) Multicolor\n
                Definition: THREE or more colors used prominently, evenly distributed, without SINGLE dominance. Clearly multi-hue print, rainbow-colored art prints. Prints clearly dominated by 1 or 2 main colors. No single predominant hue clearly identified.\n

                Conditions:\n
                1) Return the 1st color as most dominant color in terms of coverage, 2nd color as the second most dominant color in terms of coverage.\n
                2) If there exists more than 3 colors Return Most dominant colors as 1st choice, 2nd choice and then followed by Multicolor.\n"""}


Keywords_def = {"""You are an expert art curator. Your task is to distill the essence of an artwork into a concise list of its most impactful keywords. **The goal is quality, not quantity.** It is far better to provide 3-5 perfect keywords that "paint the right picture" than a long list of mediocre ones.\n

                Your keywords must go beyond the basic information already provided by the `Subject`, `Medium`, `Style`, and `Color` attributes. Your primary goal is to create a diverse and balanced set of keywords that reveals the artwork's core story and feeling.\n

                To generate the best keywords, think through the following categories. **Your final list should be a thoughtful selection from these areas, not an exhaustive list from every category.**\n

                **1. Concrete Subjects & Elements:**\n
                - What are the specific, tangible objects or figures depicted? Go beyond the broad `Subject` category.\n
                - *Example: If `Subject` is "Still Life," your keywords could be "vintage camera," "stacked books," or "antique globe." If `Subject` is "Animals," a keyword could be "majestic lion" or "soaring eagle."*\n

                **2. Theme & Concept (The "Big Idea"):**\n
                - What is the central message, story, or idea? What underlying themes are explored?\n
                - Think about concepts like: `solitude`, `growth`, `nostalgia`, `urban energy`, `nature's tranquility`, `human connection`, `adventure`, `dreamscape`.\n

                **3. Mood & Emotional Vibe (The Feeling):**\n
                - What is the dominant atmosphere? What feelings does the artwork evoke?\n
                - Use descriptive words like: `calming`, `serene`, `energetic`, `meditative`, `moody`, `whimsical`, `uplifting`, `mysterious`, `romantic`, `sophisticated`.\n

                **4. Descriptive Aesthetics & Composition:**\n
                - How is the art executed? What are its unique visual qualities? This is your chance to add nuance to the `Style` attribute.\n
                - Think about: `dynamic composition`, `intricate detail`, `bold linework`, `minimalist form`, `ethereal quality`, `textural details`, `symmetrical balance`, `dramatic lighting`, `soft focus`.\n

                **5. Ideal Placement & Purpose:**\n
                - Where would this art feel at home? What purpose does it serve?\n
                - Keywords could include: `statement piece`, `gallery wall`, `office decor`, `nursery art`, `conversation starter`, `meditation space`, `reading nook accent`.\n

                ---

                **CRITICAL INSTRUCTIONS & CONSTRAINTS:**\n

                *   **AVOID KEYWORD STUFFING:** This is the most important rule. **Do not add keywords just to meet a count.** Every single keyword must add unique and significant value. If only 4 keywords truly capture the art, provide only 4. Aim for **4-15 keywords in most cases**.\n
                *   **AIM FOR DIVERSITY:** Your final keyword list must be a balanced blend. Do not pull all keywords from a single category (e.g., don't make them all about emotion). Touch upon the most relevant facets to give a full profile.\n
                *   **DO NOT** simply repeat the *broad category names* of the `Subject`, `Medium`, `Style`, or `Color` attributes. **However, you should provide specific and detailed keywords that elaborate on these categories.** For example, if `Subject` is "Animals," a keyword like "majestic lion" or "octopus" is highly encouraged. If `Style` is "Minimalism," a good keyword is "uncluttered" or "simple living," not "minimalist."\n
                *   **DO NOT** use brand names, product names, celebrity names, artist names, movie names, or specific titles of movies, books, or songs. The keywords must be generic and thematic.\n
                *   **DO NOT** use names of specific cities, countries, or famous landmarks unless they are absolutely generic in representation.\n

                ---
                **EXAMPLE OF HOW TO APPLY THIS:**\n

                **Artwork:** A dark, moody photograph of a single fern leaf with water droplets against a black background.\n
                *   **Attributes:** `Subject: Plants`, `Medium: Photography`, `Style: Minimalism`, `Color: Black, Green`\n

                *   **POOR Keywords (Keyword Stuffing):** `plant`, `photography`, `minimalist`, `black`, `green`, `fern`, `leaf`, `calm`, `serene`, `peaceful`, `tranquil`, `meditative`, `quiet`, `soothing`. (This is a long, low-value list).\n

                *   **EXCELLENT Keywords (Concise & Impactful):** `moody nature`, `serene simplicity`, `macro detail`, `dramatic lighting`, `resilience`, `zen decor`, `dark academia`, `contemplative art`.\n
                    *   **(Notice how this concise list of 8 keywords is powerful and diverse. It captures the artwork's essence from multiple angles—mood, style, detail, theme, and purpose—without any filler. This is the balance and precision you must achieve.)**\n
                
                *   **Return your response in the exact JSON format as follows:**\n
                    *   ** Keywords": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}]** \n

                **Your final output should be a single comma-separated list of the most essential keywords, typically between 4 and 8.**"""}