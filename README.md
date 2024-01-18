# Projekta nosaukums
Vietnes funkcijas automatizācija

## Projekta uzdevums
Šis projekts ir paredzēts lai automatizētu lietotāja pieteikšanos izspēlēs vietnē Scrap.tf, tās galvenais mērķis ir vienkāršot izspēles dalības procesu, samazinot nepieciešamību manuāli atvērt un pieteikties izspēlēs. Šī sistēma ļauj lietotājiem ietaupīt laiku, automatizējot ikdienas darbības.

## Izmantotās Python bibliotēkas un to izvēles pamatojums
Projektā tiek izmantotas šādas Python bibliotēkas:
- 'selenium': lai automatizētu tīmekļa pārlūkošanu un lietotāja darbības. Šī bibliotēka ļauj programmatiski atdarināt lietotāja darbības tīmekļa lapā, kas nepieciešama, lai automatizētu izspēlēs dalību.
- 'undetected_chromedriver': lai apietu vietņu automatizācijas aizsardzības mehānismus. Šī bibliotēka nodrošina, ka pārlūkošanas sesija ir vairāk kā reāla lietotāja sesija, samazinot bloķēšanas iespējamību, izmantojot automatizāciju.
- 'time': lai nodrošinātu laika aizkaves funkciju, kas var būt nepieciešama procesu sinhronizēšanai.

## Programmatūras izmantošanas metodes
Lai izmantotu šo programmatūru, lietotājam jāievada akreditācijas dati, jāpalaiž skripts un jāļauj viņam veikt nepieciešamās darbības. Skripts atvērs pārlūkprogrammu, pieteiksies Scrap.tf, apmeklēs Raffles lapu un automātiski tiks iekļauts lietotājam pieejamo Raffles sarakstā.
