test_info=[

    {
        "name": "SHAXS EMOTSIONAL INTELLEKTINING SIFATLARINING PSIXOLOGIK TASHXISI",
        "desc": "G. Ayzenkning “Psixik holatlarda o'z-o'zini baholash”",
        "variants": [
            {
                "name": "Xavotirlanish",
                "index": "1-10",
                "variants": [
                    {
                        "name": 7,
                        "desc": "Sizda xavotirlanish darajasi past chiqdi. Xavotirlilik past bo’lganda siz oldinga dadil qadam tashlay olasiz va qiyinchiliklardan qo’rqmaysiz. Omadsizlikka duch kelishingiz mumkinligidan xavotirga tushmaysiz;"
                    },
                    {
                        "name": 14,
                        "desc": "Sizda xavotirlanishning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda uning yakuni haqida xavotirga tushasiz. Bu esa sizning faoliyatingiz unumdorligini pasayishiga olib kelishi mumkin;"
                    },
                    {
                        "name": 20,
                        "desc": "Sizda xavotirlanishning yuqori darajasi mavjud. Xavotirlik darajasi yuqori bo’lsa, sizning shaxsiy va mehnat faoliyatingizda bir qancha qiyinchiliklar yuzaga kelishi mumkin. Doimiy xavotir ostida yashash esa doimiy stressga, shaxslararo munosabatlarning buzilishiga olib kelishi mumkin."
                    }
                ]
            },
            {
                "name": "Umidsizlik",
                "index": "11-20",
                "variants": [
                    {
                        "name": 7,
                        "desc": "Sizda umidsizlik darajasi past chiqdi. Umidsizlik past bo’lganda siz o’z oldingizga katta maqsadlarni qo’ya olasiz va katta yutuqqa erishihdan umid qilasiz. Bu uchun tinimsiz mehnat qilishdan qo’rqmaysiz."
                    },
                    {
                        "name": 14,
                        "desc": "Sizda umidsizlikning o’rta darajasi aniqlandi. Siz biror bir faoliyatni amalga oshirayotganda uning yakuni siz kutgan natijani bermasligi mumkinligidan ba’zan umidsizlikka tushasiz. Bu esa o’z o’zidan xavotirlik, tashvish hissini yuzaga keltirishi mumkin."
                    },
                    {
                        "name": 20,
                        "desc": "Sizda umidsizlikning yuqori darajasi mavjud. Umidsizlik darajasi yuqori bo’lsa, siz o'zingizni past baholaysiz, qiyinchiliklardan qochasiz, muvaffaqiyatsizliklardan qo'rqasiz va umidsizlikka tushasiz."
                    }
                ]
            },
            {
                "name": "Agressivlik",
                "index": "21-30",
                "variants": [
                    {
                        "name": 7,
                        "desc": "Sizda agressiyaning darajasi past ekanligi aniqlandi. Agar agressiya (tajavuzkorlik) darajasi past bo’lsa siz insonlar bilan muloqotga kirishishda, o’zingizni boshqarishda hech qanday qiyinchiliklarga duch kelmaysiz."
                    },
                    {
                        "name": 14,
                        "desc": "Sizda agressiyaning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda, odamlar bilan muloqotga kirishayotganda qiyinchiliklarga duch kelasiz. Arzimasa-dek tuyilgan narsalarga tez asabiylashasiz. Bu esa sizning faoliyatingizni bir me’yorda kechishiga xalaqit berishi mumkin."
                    },
                    {
                        "name": 20,
                        "desc": "Sizda agressiyaning yuqori darajasi mavjud. Agressiya darajasi yuqori bo’lsa, siz atrofingizdagilar bilan doimiy nizolashasiz, o’z hissiyotlaringizni boshqarishga qiynalasiz. Bu esa o’zidan atrofdagilan bilan munosabatlaringizni yomonlashishiga olib keladi. Ushbu holatdan chiqish uchun o’z hissiyotlaringizni, g’azabingizni boshqarishga harakat qiling."
                    }
                ]
            },
            {
                "name": "Qat’iyatlilik",
                "index": "31-40",
                "variants": [
                    {
                        "name": 7,
                        "desc": "Sizda qat’iyatlilikning darajasi past. Agar qat’iyatlilik darajasi past bo’lsa siz o’z oldingizga qo’ygan maqsadlaringiz, rejalaringizga erishishda qiynalishingiz mumkin."
                    },
                    {
                        "name": 14,
                        "desc": "Sizda qat’iyatlilikning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda, ko’plab ikkilanishlarga, qo’rquvlarga duch kelasiz. Bularning barchasi sizda qilayotgan ishingizga nisbatan qat’iyat bilan yondasholmasligingiz sabab. Agar o’z qat’iyatliligingiz ustida ishlasangiz bunday muammolarga yechim topgan bo’lasiz."
                    },
                    {
                        "name": 20,
                        "desc": "Sizda qat’iyatlilikning yuqori darajasi mavjud. Qat’iyatlilik darajasi yuqori bo’lsa, siz barcha maqsadlaringiz, o’z qarorlaringizni amalga oshirishda qiyinchiliklarga duch kelish ehtimoli keskin past bo’ladi. Bu esa sizni muvaffaqiyatga erishishingizga zamin yaratadi."
                    }
                ]
            }
        ]
    }
]
questions_emotion = [
    {'question': "Men o’zimga nisbatan ishonchni his qilmayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 1},

    {'question': "Men tez-tez arzimas narsalardan qizarib ketaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 2},

    {'question': "Mening uyqum notinch",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 3},

    {'question': "Men osongina tushkunlikka tushaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 4},

    {'question': "Men faqat xayoliy muammolar haqida qayg'uraman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 5},

    {'question': "Qiyinchiliklar meni qo'rqitadi",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 6},

    {'question': "Men o'z kamchiliklarimni ko'rib chiqishni yaxshi ko'raman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 7},

    {'question': "Meni biror narsaga ishontirish oson",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 8},

    {'question': "Men ko’p narsadan shubhalanaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 9},

    {'question': "Biror narsani kutishda qiynalaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 10},

    {
        'question': "Ko'pincha vaziyatlar men uchun umidsiz bo'lib tuyuladi, garchi undan chiqish yo'lini topish hali mumkin bo’lsa ham",
        'answers': [
            {'name': 'Sizda tez-tez uchrasa', 'value': 2},
            {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
            {'name': "hech qachon sodir bo'lmasa", 'value': 0}
        ], 'index': 11},

    {'question': "Muammolar meni juda xafa qiladi, men ruhan tushkunlikka tushaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 12},

    {'question': "Katta muammolar yuzaga kelganda, men hech qanday sababsiz o'zimni ayblashga moyilman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 13},

    {'question': "Baxtsizliklar va muvaffaqiyatsizliklar menga hech narsani o'rgatmaydi",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 14},

    {'question': "Men ko'pincha kurashishni samarasiz deb hisoblayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 15},

    {'question': "Ko'pincha o'zimni himoyasiz his qilaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 16},

    {'question': "Ba'zida men umidsizlikka tushib qolaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 17},

    {'question': "Qiyinchiliklar oldida sarosimaga tushman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 18},

    {
        'question': "Hayotning og'ir damlarida ba'zan o'zimni bolalarcha tutaman, odamlarning menga achinishlarini xohlayman",
        'answers': [
            {'name': 'Sizda tez-tez uchrasa', 'value': 2},
            {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
            {'name': "hech qachon sodir bo'lmasa", 'value': 0}
        ], 'index': 19},

    {'question': "Men xarakterimdagi kamchiliklarni tuzatib bo'lmaydigan deb bilaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 20},

    {'question': "Ma’lum bir vaziyatda oxirgi so’zni men aytaman (ya’ni qaror qabul qilish o’z qo’limda bo’ladi)",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 21},

    {'question': "Ko'pincha suhbatda men suhbatdoshimni gapini bo’laman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 22},

    {'question': "Meni osongina jahlim chiqaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 23},

    {'question': "Men boshqalarning kamchiliklariga izoh berishni yaxshi ko'raman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 24},

    {'question': "Men boshqalar uchun avtoritetda bo'lishni xohlayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 25},

    {'question': "Men oz narsaga qanoat qilmayman, ko'p narsani xohlayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 26},

    {'question': "G‘azablansam, o‘zimni boshqara olmayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 27},

    {'question': "Men itoat qilishdan ko'ra rahbarlikni afzal ko'raman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 28},

    {'question': "Menda keskin, qo'pol imo-ishoralar bor",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 29},

    {'question': "Men qasoskorman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 30},

    {'question': "Menga odatlarni o'zgartirishim qiyin",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 31},

    {'question': "Diqqatni o'zgartirish oson emas",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 32},

    {'question': "Men hamma yangi narsalarga nisbatan juda ehtiyotkorman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 33},

    {'question': "Meni ishontirish qiyin",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 34},

    {'question': "Ko'pincha men voz kechish kerak bo’lgan fikrni boshimdan chiqara olmayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 35},

    {'question': "Odamlarga yaqinlashish men uchun oson emas",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 36},

    {'question': "Rejadagi kichik buzilishlar ham meni xafa qildi",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 37},

    {'question': "Men tez-tez qaysarlik qilaman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 38},

    {'question': "Men tavakkal qilishni istamayman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 39},

    {'question': "Men kundalik tartibdagi o’zgarishlar haqida juda ham qayg’uraman",
     'answers': [
         {'name': 'Sizda tez-tez uchrasa', 'value': 2},
         {'name': "Vaqti-vaqti bilan sodir bo'lsa", 'value': 1},
         {'name': "hech qachon sodir bo'lmasa", 'value': 0}
     ], 'index': 40}
]
