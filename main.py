import xmltodict
import math

from ChildNode import *

with open('products.xml', 'r') as f:
    data = f.read()

xml_data = xmltodict.parse(data)
products = xml_data['products']

html = ChildNode('html', value='en', key='lang')

# ------------------ HEAD
head = html.add_element('head')
meta = head.add_element('meta', key='charset', value='UTF-8')
title = head.add_element('title', data='Title')
link = head.add_element('link', 'href',
                        "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap")
link.add_attribute('rel', "stylesheet")
link1 = head.add_element('link', 'rel', "stylesheet")
link1.add_attribute('href', "tw.css")
# ------------------ HEAD

# ------------------ BODY
body = html.add_element('body')

# ------------------ HEADER
header = body.add_element('header')
div = header.add_element('div', 'class', 'relative overflow-hidden bg-cover bg-no-repeat')
div.add_style('background-position: 50%; height: 200px;')
div1 = div.add_element('div', 'class', 'absolute bottom-0 left-0 right-0 top-0 h-full w-full overflow-hidden bg-fixed')
div1.add_style('background-color: rgba(0, 0, 0, 0.8)')
div2 = div1.add_element('div', 'class', "flex h-full items-center ")
div3 = div2.add_element('div', 'class', "px-6  md:px-12")
h1_1 = div3.add_element('h1', 'class', "mb-4 text-6xl font-bold text-gray-200", "Bryan Movie's review")
# ------------------ HEADER

# ------------------ CONTAINER
container = body.add_element('div', 'class', 'container my-24 mx-auto md:px-6')

dv = {}
for i, product in enumerate(products['product']):
    interview_count = len((product['reviews']['review'])) if 'reviews' in product else 0
    interview_box_counts = math.ceil(len((product['reviews']['review'])) / 2) if interview_count else 0

    dv[f'div_{i}'] = container.add_element('div', 'class', 'my-20')
    dv[f'section_{i}'] = dv[f'div_{i}'].add_element('section', 'class', 'mb-32')
    dv[f'div_1_{i}'] = dv[f'section_{i}'].add_element('div', 'class', 'flex flex-wrap lg:px-20')
    dv[f'div_2_{i}'] = dv[f'div_1_{i}'].add_element('div', 'class',
                                                    'w-full shrink-0 grow-0 basis-auto md:w-2/12 lg:w-3/12')
    dv[f'img_{i}'] = dv[f'div_2_{i}'].add_element('img', 'class',
                                                  'mb-6 w-full rounded-lg shadow-lg dark:shadow-black/20')
    dv[f'img_{i}'].add_attribute('src', product['image'])

    dv[f'div_3_{i}'] = dv[f'div_1_{i}'].add_element('div', 'class',
                                                    'w-full shrink-0 grow-0 basis-auto text-center md:w-10/12 md:pl-6 md:text-left lg:w-9/12')
    dv[f'h_{i}'] = dv[f'div_3_{i}'].add_element('h5', 'class', 'mb-6 text-3xl  font-semibold',
                                                product['summary']['h3'])
    dv[f'p_{i}'] = dv[f'div_3_{i}'].add_element('p', data=product['summary']['p'])

    dv[f'section_1_{i}'] = dv[f'div_{i}'].add_element('section', 'class',
                                                      'rounded-md p-6 text-center shadow-lg md:p-12 md:text-left')
    dv[f'section_1_{i}'].add_attribute('style', "background-image: url(images/background3.jpg)")

    dv[f'div_4_{i}'] = dv[f'section_1_{i}'].add_element('div', 'class', 'mx-auto text-center md:max-w-xl lg:max-w-3xl')
    dv[f'h3_1_{i}'] = dv[f'div_4_{i}'].add_element('h3', 'class', 'mb-6 text-4xl font-bold text-gray-100',
                                                   'Movie reviews')

    interview_counter = 0
    should_exit = False

    for j in range(interview_box_counts):
        dv[f'div_5_{i}_{j}'] = dv[f'section_1_{i}'].add_element('div', 'class',
                                                                'flex justify-center flex-wrap lg:flex-nowrap')
        for k in range(2):
            interview_counter += 1
            interview = product['reviews']['review'][interview_counter - 1]
            dv[f'div_6_{i}_{j}_{k}'] = dv[f'div_5_{i}_{j}'].add_element('div', 'class', 'max-w-3xl')
            dv[f'div_7_{i}_{j}_{k}'] = dv[f'div_6_{i}_{j}_{k}'].add_element('div', 'class',
                                                                            'm-4 block rounded-lg bg-white p-6 shadow-lg dark:bg-neutral-800 dark:shadow-black/20')
            dv[f'div_8_{i}_{j}_{k}'] = dv[f'div_7_{i}_{j}_{k}'].add_element('div', 'class', 'md:flex md:flex-row')
            dv[f'div_9_{i}_{j}_{k}'] = dv[f'div_8_{i}_{j}_{k}'].add_element('div', 'class', 'md:ml-6')
            dv[f'p_{i}_{j}_{k}'] = dv[f'div_9_{i}_{j}_{k}'].add_element('p', 'class',
                                                                        'text-xl font-semibold  pb-3 text-gray-700',
                                                                        interview['title']
                                                                        )

            dv[f'p_1_{i}_{j}_{k}'] = dv[f'div_9_{i}_{j}_{k}'].add_element('p', 'class',
                                                                          'mb-6 font-light text-neutral-500 dark:text-neutral-300',
                                                                          interview['text']
                                                                          )
            dv[f'p_2_{i}_{j}_{k}'] = dv[f'div_9_{i}_{j}_{k}'].add_element('p', 'class',
                                                                          'font-semibold text-neutral-600 dark:text-neutral-200',
                                                                          interview['writer'],
                                                                          data_first=True
                                                                          )

            dv[f'span_{i}_{j}_{k}'] = dv[f'p_2_{i}_{j}_{k}'].add_element('span', 'class',
                                                                         'mb-0 inline text-sm text-neutral-500 dark:text-neutral-400',
                                                                         f"({interview['place']})"
                                                                         )

            dv[f'h6_{i}_{j}_{k}'] = dv[f'div_9_{i}_{j}_{k}'].add_element('h6', 'class',
                                                                         'mb-4 text-sm font-semibold text-primary dark:text-primary-500',
                                                                         interview['date']
                                                                         )

            dv[f'ul_{i}_{j}_{k}'] = dv[f'div_9_{i}_{j}_{k}'].add_element('ul', 'class', 'mb-0 flex')

            stars = int(interview['stars'])

            for star in range(stars):
                dv[f'li_{i}_{j}_{k}_{star}'] = dv[f'ul_{i}_{j}_{k}'].add_element('li')
                dv[f'svg_{i}_{j}_{k}_{star}'] = dv[f'li_{i}_{j}_{k}_{star}'].add_element('svg', 'viewBox', '0 0 24 24')
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('fill', "currentColor")
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('class', "h-5 w-5 text-yellow-500")
                dv[f'path{i}_{j}_{k}_{star}'] = dv[f'svg_{i}_{j}_{k}_{star}'].add_element('path', 'fill-rule',
                                                                                          'evenodd')
                dv[f'path{i}_{j}_{k}_{star}'].add_attribute('d',
                                                            "M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.007 5.404.433c1.164.093 1.636 1.545.749 2.305l-4.117 3.527 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.117-3.527c-.887-.76-.415-2.212.749-2.305l5.404-.433 2.082-5.006z")
                dv[f'path{i}_{j}_{k}_{star}'].add_attribute('clip-rule', "evenodd")

            for star in range(5 - stars):
                dv[f'li_{i}_{j}_{k}_{star}'] = dv[f'ul_{i}_{j}_{k}'].add_element('li')
                dv[f'svg_{i}_{j}_{k}_{star}'] = dv[f'li_{i}_{j}_{k}_{star}'].add_element('svg', 'viewBox', '0 0 24 24')
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('fill', "none")
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('class', "h-5 w-5 text-yellow-500")
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('stroke-width', "1.5")
                dv[f'svg_{i}_{j}_{k}_{star}'].add_attribute('stroke', "currentColor")
                dv[f'path{i}_{j}_{k}_{star}'] = dv[f'svg_{i}_{j}_{k}_{star}'].add_element('path', 'stroke-linecap',
                                                                                          'round')
                dv[f'path{i}_{j}_{k}_{star}'].add_attribute('stroke-linejoin', "round")
                dv[f'path{i}_{j}_{k}_{star}'].add_attribute('d',
                                                            "M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z")

            if interview_counter == interview_count:
                should_exit = True
                break

        if should_exit:
            break

        dv[f'div_6_{i}_{j}'] = dv[f'div_5_{i}_{j}'].add_element('div', 'class', 'max-w-3xl')

footer = body.add_element('footer', 'class',
                          'flex flex-col items-center bg-neutral-200 text-center text-white dark:bg-neutral-600 dark:text-neutral-200')
div5 = footer.add_element('div', 'class', 'container p-6')
div6 = div5.add_element('div', 'class', 'grid gap-4 md:grid-cols-3 lg:grid-cols-10')

footer_images = [
    'images/3.jpg',
    'images/animal.jpg',
    'images/blue_eye_samurai.jpg',
    'images/oppenheimer.jpg',
    'images/adam_sandler.jpg',
    'images/killer.jpg',
    'images/trolls.jpg',
    'images/thanksgiving.jpg',
    'images/vidho_vind.jpg',
    'images/godzilla.jpg',
]

fi = {}
for image in footer_images:
    fi[f'div_{image}'] = div6.add_element('div', 'class', 'mb-6 lg:mb-0')
    fi[f'img_1_{image}'] = fi[f'div_{image}'].add_element('img', 'class', 'w-full rounded-md shadow-lg')
    fi[f'img_1_{image}'].add_attribute('src', image)

div7 = footer.add_element(
    'div',
    'class',
    'w-full bg-neutral-300 p-4 text-center text-neutral-700 dark:bg-neutral-700 dark:text-neutral-200',
    '&#169; 2023 Copyright:',
    True
)

div7.add_element('a', 'class', 'dark:text-neutral-400', "Bryan Movie's review")
script = body.add_element('script', 'src', 'tw.js')
script1 = body.add_element('script',
                           data=' tailwind.config = {darkMode: "class",theme: {fontFamily: {sans: ["Roboto", "sans-serif"],body: ["Roboto", "sans-serif"],; mono: ["ui-monospace", "monospace"],},}, corePlugins: { preflight: false,},}')

execute(html)
