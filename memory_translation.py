PAGE_SIZE = 1024
PAGE_TABLE = {
    0: 5,
    1: 2,
    2: 9,
    3: 1
}
SEGMENT_TABLE = {
    0: (1000, 400),
    1: (2200, 300),
    2: (500, 150)
}

def translate_page(address):
    page_number = address // PAGE_SIZE
    offset = address % PAGE_SIZE
    if page_number not in PAGE_TABLE:
        print(
            "Logical address:",
            address,
            "-> Page fault"
        )
        return
    frame_number = PAGE_TABLE[page_number]
    physical_address = (
        frame_number * PAGE_SIZE + offset
    )
    print(
        "Logical address:",
        address,
        "-> Physical address:",
        physical_address
    )

def translate_segment(segment, offset):
    if segment not in SEGMENT_TABLE:
        print(
            "Segment:",
            segment,
            "-> Segmentation fault"
        )
        return
    base = SEGMENT_TABLE[segment][0]
    limit = SEGMENT_TABLE[segment][1]
    if offset >= limit:
        print(
            "Segment:",
            segment,
            "Offset:",
            offset,
            "-> Segmentation fault"
        )
        return
    physical_address = base + offset
    print(
        "Segment:",
        segment,
        "Offset:",
        offset,
        "-> Physical address:",
        physical_address
    )

print("PAGING")
print("-" * 40)
translate_page(260)
translate_page(1500)
translate_page(3000)
translate_page(5000)

print("\nSEGMENTATION")
print("-" * 40)
translate_segment(0, 150)
translate_segment(1, 350)
translate_segment(2, 100)

