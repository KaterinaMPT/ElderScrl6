colza = {"drakon": "1", "volk": "1", "babochka": "3"}
inventar = ["Секира Довакина", "Драконья броня", "Сапфировый коготь"]
inventartorg = ["Сильное зелье лечения", "Амулет Диабеллы", "Противоядие"]
print ("Здравстуйте, странник! Эта игра посвящена великой серии игр The Elder Scrolls(а именно, Скайриму)")
print ("Действия происходят в деревне Ривервуд. Вы - Довакин, отошедший от дел. Эра ваших приключений давно окончена")
print ("Но по деревне разносятся слухи о новом подземелье, что недавно буквально изниоткуда появилось в ее округе")
print ("Ваш друг - торговец Лукан Валерий вручает Вам сапфировый коготь дракона")
print ("Вспоминая свою молодость, времена, когда Вы путешествовали по миру и сражались с драконами, вы думаете, что это - знак")
print ("Вперед, Довакин, покорите Сапфировое подземелье!")
print ("Используйте сапфировый коготь дракона, чтобы попасть к главному сокровищу!\n")
name = input("Введите имя: ").capitalize()
print ("\nПринимаете ли вы этот вызов,",name,"?")
print("Введите да, чтобы принять вызов, введите любую другую клавишу, чтобы отклонить")
vxodvixod = input().capitalize()

def menu(vxodvixod):
    if vxodvixod == "Да" :
     print ("\nВы стоите на главной тропе Ривервуда, выбирая куда следует пойти")
     print("1. \"Ривервудский торговец\"\n2. Таверна \"Спящий великан\"\n3. Сапфировое подземелье ")
     print("Куда пойдете?")
     try:
      pyti = int (input()) 
      match pyti:    
        case 1:
         print("\nВеликий Довакин отправляется к Лукану Валерию!")
         def lucan(inventar, inventartorg):
           print("Вы заходите в торговую лавочку с приятной домашней атмосферой.\nКамилла подметает деревянный пол, шаркая метлой, в то время как её брат стоит за торговой стойкой.")
           print(f"Камилла: \"Снова здравствуй, {name}, проходи\"\nДевушка спешно отступает вправо, пропуская Вас к стойке ")
           print(f"Лукан: \"{name}, ну как там с подземельем?! Удалось раскрыть его секреты? Чего нужно?\"")
           print("В торговой лавке вы можете: \n1. Поговорить с владельцем \n2. Купить что-либо")
           lavka = int (input()) 
           match lavka:
             case 1:
               print("\nЛукан: \"Поговорить хочешь? Конечно, друг! Что хочешь узнать?\"")
               vopros = int (input("Спросить о... \n 1. \"Сапфировый коготь\" \n 2. \"Подземелье\" \n 3. \"Лукан\"\n"))
               match vopros:
                case 1:
                 print("\nЛукан: \"О, этот занятный ключ.. Помнишь такой же золотой, который у меня украли в прошлый раз? \nТогда без твоей помощи я бы его не вернул! \nЭтот такой же.. Открывает какую-то дверь. Найди ее\"")
                 print("Обогащенный новыми знаниями, Довакин выходит из лавки")
                 menu(vxodvixod)
                case 2:
                 print("\nЛукан: \"Подземелье.. Просто появилось тут однажды. \nЯ не знаю что там, я не герой\"")
                 print("Обогащенный новыми знаниями, Довакин выходит из лавки")
                 menu(vxodvixod)
                case 3:
                 print(f"\nЛукан: \"Обо мне? Да чего ты обо мне не знаешь, {name}? \nЯ имперец, живу тут с сестрой, торгую вещами. \nКто-то зовет мой товар мусором, но для меня это сокровища. ")
                 print("Обогащенный новыми знаниями, Довакин выходит из лавки")
                 menu(vxodvixod)
                case _:
                    print("Лукан: \"Не понимаю о чем ты говоришь. Иди проспись\"")
                    menu(vxodvixod)
             case 2:
                print("\nСписок товаров: \n1. \"Сильное зелье лечения\" - 100 септимов \n2. \"Противоядие\" - 50 септимов \n3. \"Амулет\" - 100 септимов")
                tovar = int (input())
                match tovar:
                 case 1:
                    if "Сильное зелье лечения" in inventartorg:
                     print("\nЛукан: \"Это точно понадобится в борьбе с драуграми! Мудрое решение\"")
                     inventar.append("Сильное зелье лечения")
                     inventartorg.remove("Сильное зелье лечения")
                     print("В Вашем инвентаре появилось зелье лечния! Из Вашего кошелька убыло 100 септимов.\n Довольный Довакин покидает лавку!")
                     print("Ваш инвентарь:",inventar)                                    
                     menu(vxodvixod)
                    else:
                      print("\nВаш инвентарь:",inventar)    
                      print("Лукан: \"У меня закончились, прости, друг\"")
                      print("В расстроенных чувствах Довакин в слезах выбегает из лавки")
                      menu(vxodvixod)                            
                 case 2:       
                    if "Противоядие" in inventartorg:                              
                     print("\nЛукан: \"Боишься встретить пауков? Правильно боишься! Говорят, они встречаются там, где много мха..\"")
                     inventar.append("Противоядие")
                     inventartorg.remove("Противоядие")
                     print("В Вашем инвентаре появляется противоядие! Из кошелька убыло 50 септимов.\n Довольный Довакин покидает лавку!") 
                     print("Ваш инвентарь:",inventar)    
                     menu(vxodvixod)
                    else:
                      print("\nВаш инвентарь:",inventar)    
                      print("Лукан: \"Тебя так часто кусают? У меня закончились, прости, друг\"")
                      print("В расстроенных чувствах Довакин в слезах выбегает из лавки")
                      menu(vxodvixod)                                                           
                 case 3: 
                    if "Амулет Диабеллы" in inventartorg:                                
                     print("\nЛукан: \"Амулет Диабеллы? Хочешь заговорить кому-то зубы? Главное, что ты не поклоняешься Талосу...\" ")
                     inventar.append("Амулет Диабеллы")
                     inventartorg.remove("Амулет Диабеллы")
                     print("В Вашем инвентаре появляется Амулет Диабеллы! Из кошелька убыло 100 септимов.")   
                     print("Ваш инвентарь:",inventar)                
                     menu(vxodvixod)  
                    else:
                      print("\nВаш инвентарь:",inventar)    
                      print("Лукан: \"Какой ярый поклонник... У меня закончились, прости, друг\"") 
                      print("В расстроенных чувствах Довакин в слезах выбегает из лавки")
                      menu(vxodvixod)
                 case _:
                   print("\nЛукан: \"У меня нет такого товара\"")
                   print("С горя, осознав, что никто не понимает Вашей гениальности, Вы выходите из лавки")
                   menu(vxodvixod)
             case _:
               print("\nЛукан: \"Тут не о чем говорить\"")
               print("С горя, осознав, что никто не понимает Вашей гениальности, Вы выходите из лавки")
               menu(vxodvixod)
         lucan(inventar, inventartorg)

        case 2:
         print("\nВеликий Довакин отправляется в Таверну!")
         print("По пути Вы встречаете камень прямо у стены таверны. Внутри Вас просыпается неописуемо сильное желание его пнуть.")
         print("Поддасться соблазну?\n1.Да\n2.Нет")
         camen = int (input())
         match camen:
           case 1:
             print("\n------------------------------Секретная концовка------------------------------")
             print("Поддавшись соблазну, вы замахиваетесь ногой и со всей силы ударяете по камню.\nВидимо, не рассчитав свои возможности, Вы позабыли об осторожности.")
             print("Камень рекошетит прямо от стены и прилетает в вашу голову, аккурат в висок.")
             print(f"Да, {name}, никто и не думал, что Великий Довакин лишится жизни по собственной глупости...")
             b = input()
             exit()
           case 2:
             print("\nУ Вас получается преодолеть невыносимое желание пнуть бедный камень. Что-то подсказывает вам, что это верное решение.")
             print("Подойдя к таверне, вы вдруг понимаете, что сегодня тут закрыто. Какая жалость")
             menu(vxodvixod)
           case _:
             print("\nНичего так и не решив, Вы возвращаетесь назад")
             menu(vxodvixod)
        case 3:
         print("\nНе помрите, Великий Довакин! Лучше закупиться перед подземельем!")
         def podzemelie(inventar):
           print("\nВаш инвентарь:",inventar) 
           print("Протиснувшись через расщелину в скале, Вы оказываетесь в тускло освещаемом помещении")
           print("За недолгое время здесь побывало множество путешественников, желающих лёгкой наживы \nПоэтому главная \"зала\" увешана факелами, а посреди стоит небольшой стол, стулья, да пара сундуков ")
           print("Если оглядеться, становится ясно, что дальше есть только три прохода. \nКакой-то заботливый проходимец подписал две расщелины")
           print("Куда пойдете,", name, "?" "\n1. ДРАУГРЫ \n2. ПОЛЗУЧИЕ ТВАРИ \n3. ? \n4. Назад." )
           vxod = int (input())       
           match vxod:
              case 4:
               print("\nТрус-Довакин выбегает в страхе! Не потеряйте секиру, ",name,"!")
               menu(vxodvixod)
              case 1:
               print("\nВы проходите в тёмную расщелину. \nАтмосфера наводит лёгкий ужас..")
               print("За тонкой каменной \"Стенкой\" слышны странные звуки, отдалённо напоминающие человеческую речь и звон лат да оружия. \nПравда произносимые слова, кажется, на драконьем языке")
               print("Что будет делать великий Довакин", name,"? \n1. Пойти вперед \n2. Пойти назад")
               try:
                chtodalshe = int (input())
                if chtodalshe == 1:
                 print("\nБудучи бесстрашным Довакином, прошедшим через много бед, Вы аккуратно ступаете дальше, попутно достав свою любимую секиру. \nПодготовившись к бою, Вы входите в новое помещение")
                 print("Комната гробницы встречает Вас неожиданно ярким светом. Запах здесь затхлый, насквозь пропитанный мертвечиной. \nВы закрываете забрало шлема, как вдруг слева на Вас налетает оживший \"зомби\"") 
                 print("Но Вас не проведешь! Метким ударом Вы сносите твари голову, словно палач, встречающий посетителей Солитьюда у самых ворот. \nПравда, показательная казнь не проходит незамеченной")
                 print("Уже через несколько секунд, толпа драугров слетается со всех углов гробницы. \nПрямо перед Вами они вылезают из своих склепов да встают из могил, пробудившись после долгого сна")
                 print("С огромным трудом вы расправляетесь с каждым. Но последний драугр-палач застает Вас врасплох. Ваша жизнь вот-вот оборвется. \nБыли ли Вы достаточно предусмотрительны, чтобы потратиться на зелье восстановелния,", name, "?")
                 print("Вы можете: \n1. Использовать зелье \n2. Ожидать смерти")
                 hilka = int (input())
                 match hilka:
                     case 1:
                      if "Сильное зелье лечения" in inventar:
                       print(f"\nВы используете зелье. Это придает Вам сил и заживляет раны. Через несколько секунд, Вы расправляетесь с Драугром. Браво, {name}!")
                       colzca()
                      else:
                        print("\nВы пытались нащупать зелье, но ничего не вышло. Меч прошел через слабое место вашшей брони, рассекая плоть. \nПожалуй, стоило посетить лавку Лукана перед походом сюда.")
                        death()
                     case 2:
                        print(f"\nВы даже не пытались ничего сделать, и просто сложили оружие. Неужели это достойно великого Довакина, {name}? \nС ликованием, Драугр ломает вашу шею")
                        death()
                     case _:
                        print("\nОбезумев от страха смерти, вы бормочете непонятные вещи. \nДраугр с удовольствием ломает вашу шею")
                        death()                                         
                if chtodalshe == 2:
                 print("\nИспугавшись рёва оживших мертвецов, Вы пятитесь обратно")
                 podzemelie(inventar) 
                else:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)
               except ValueError:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar) 
              case 2:
                print("\nВы медленно проходите в одну из расщелин. Одно ее название наталкивает на мысль о Ваших заклятых врагах.. \n\"Морозные пауки..\" - думаете Вы")
                print("Вы слышите их шипение... \nНе помешало бы противоядие.. \nЧто будете делать, Довакин? \n1. Пойти вперед\n2. Пойти назад")
                try:
                 chtodalshe2 = int (input())
                 if chtodalshe2 == 1:
                  print("\nБудучи бесстрашным Довакином, прошедшим через много бед, Вы аккуратно ступаете дальше, попутно достав свою любимую секиру. \nПодготовившись к бою, Вы входите в новое помещение")
                  print("В свою очередь, с виду эта \"Комната\" явно не создана руками человека. Обычная, замшелая пещера, словно образованная сдвигами породы. \nНо внизу Вы подмечаете дверь.. \nКакое странное подземелье. Будто бы при его создании объединились люди и природные явления ")
                  print("Пауков здесь оказалось не слишком много, но рядом все же лежало пару мертвых тел. Какие-то неудачники \nОгромный членистоногий вредитель нападает на Вас первым, а его дети - накидываются следом")
                  print("Не без трудностей, Вы расправляетесь со всей оравой. Но, находите на себе кучу отвратительной ядовитой слюны")
                  print("И так измотавшись боем, вы уже не в силах самостоятельно перенести тяжелейший недуг. Понадобится противоядие \nБыли ли вы достаточно умны для того чтобы купить противоядие?")
                  print("Вы можете: \n1. Использовать противоядие или \n2. Ожидать смерти")         
                  larinprotiv = int (input())
                  match larinprotiv:
                      case 1:
                       if "Противоядие" in inventar:        
                         print("\nВы мастерски быстро выпиваете красный бутылек противоядия. Жидкость обжигает горло, но недомогание наконец проходит. \nПобедно улыбнувшись, вы сбегаете вниз по маленькой горке и, минув кучку папортников, да других растений, подходите к двери.") 
                         print(f"Браво, {name}!")
                         colzca()                         
                       else:
                         print(f"\nКажется, Вы оставляли бутылек где-то здесь... Или, может, в этом кармане? Ах, точно! Вы завбыли его купить. Какая жалость, {name}! \nВ Ваши легкие перестает поступать воздух. Вы падаете на колени")
                         death()
                      case 2:
                        print(f"\nВы даже не пытались ничего сделать, и просто сложили оружие. Неужели это достойно великого Довакина, {name}? \nС ликованием, Драугр ломает вашу шею")
                        death()
                      case _:
                        print("\nОбезумев от страха смерти, вы бормочете непонятные вещи. \nЯд быстро достигает мозга, перекрывая Вам кислород")
                        death()                         
                except ValueError:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)                      
                if chtodalshe2 == 2:
                  print("\nИспугавшись чёртовых пауков, Вы пятитесь обратно")
                  podzemelie(inventar)
                else:
                  try:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)
                  except ValueError:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)               
              case 3:
               print("\nДовольно странный выбор.. Идти в неизведанное место - совсем не лучшая идея. \nВы вдруг слышите нечленораздельную речь, напоминающую какую-то ритуальную песню.")
               print("Что будете делать? \n1. Пойти вперед \n2. Пойти назад")               
               chtodalshe3 = int (input())
               if chtodalshe3 == 1:
                 print("\nУдивительно, но вы проходите не в какое-то пещерное образование. Перед вами целая комната, обставленная действительно по-королевски.\nПочему же она не была подписана тем заботливым путешественником?")
                 print("Длинный стол доходит чуть ли не до дальней стены. Он ломится от разных явств, а во главе сидит нечто, похожее на человека. Но не слишком.")
                 print("Существо медленно поднимает на вас голову, да неожиданно усмехается, демонстрируя Вам полусгнившие зубы. На голове его корона, увенчанная сапфирами. \nНеожиданно, вы понимаете, что добрая половина королевского обеда на столе - человеческое мясо")
                 print("Король Сапфирового подземелья: \"Человек.. Нет, драконорожденны... Наконец-то, дополнение к моему обеду.. Десерт..\"")
                 print("С двух сторон вас хватают тёмные руки, сжимая броню. Та даже слегка гнётся от натиска нечисти.")
                 print(f"Быстрее, {name}, решайте! Что вы сделаете? \n1. Попытаться убедить пропустить Вас дальше \n2. Попытаться высвободиться \n3. Ничего не делать") 
                 amulet = int (input())
                 match amulet:
                   case 1:
                     if "Амулет Диабеллы" in inventar:
                       print(f"\nБлагодаря своему невероятному дару убеждения(И, пожалуй, амулету Диабеллы), у вас получается убедить короля пропустить Вас дальше. Браво, {name}, у Вас получилось! \nВам вслед раздается недовольное скрипение, но Вы все еще живы!")
                       colzca()
                     else:
                       print(f"\nВам не удалось убедить короля пропустить Вас дальше... Стоило бы прокачать Ваш навык красноречия. Зато вы стали прекрасным десертом, {name}!")
                       death()
                   case 2:
                       print(f"\nХорошая попытка! Вами пообедали, {name}!")
                       death()
                   case _:
                       print(f"\nПохоже, Вы всегда мечтали о том, чтобы быть съеденным заживо! Поздравляю, {name}, Вы добились своей цели!")
                       death()
               if chtodalshe3 == 2:
                  print("\nИспугавшись неизведанного, Вы пятитесь обратно")
                  podzemelie(inventar)
               else:
                  try:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)
                  except ValueError:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, попадая в прежнюю комнату")
                   podzemelie(inventar)    
               podzemelie(inventar) 
              case _:
                   print("\nОт смятения, Вы говорите непонятную чушь и пятитесь назад, буквально выпадая из пещеры") 
                   menu(vxodvixod)  
         podzemelie(inventar)                   
        case _:   
          print("\nУ Вас только 3 пути... Будьте внимательнее")   
          menu(vxodvixod) 
     except ValueError:   
          print("\nНужно выбрать цифру... Будьте внимательнее")   
          menu(vxodvixod)                      
    else:
      try:
         print ("\nСлабак! Будь фермером до конца дней своих")
         b = input()
         exit()
      except ValueError:
         print("\nСлабак! Будь фермером до конца дней своих")
         b = input()
         exit()         
    return menu
def colzca():
  print("\nПеред Вами дверь с несколькими кольцами. Кажется, это загадка. \nВам нужно повернуть их так, чтобы все животные были на своем месте")
  print("На стене есть подсказка. Она гласит: \"Дракон ест волка, волк ест бабочку\". Похоже, тот, кто писал ее, был плохо знаком с законами природы.")
  print("Примечание: поверните кажде кольцо в соответствующее положение. В данный момент первым идет дракон, вторым тоже дракон, а третьей - бабочка.")
  zagadka(colza)
def zagadka(colza):
 print("\nЧто будете делать: \n1. Повернуть большое кольцо \n2. Повернуть среднее \n3. Повернуть малое")
 while colza == {"drakon": "1", "volk": "1", "babochka": "3"}:
      varik = int (input())
      match varik:
        case 1:
         while colza["drakon"] != 1:
             print("\nПервое кольцо не двигается. Видимо, оно уже находится в верном положении.")
             zagadka(colza)
         else:
          print("\nКольцо уже в правильном положении. Попробуйте другое.")
          zagadka(colza)
        case 2:
         while colza["volk"] != 2:
             print("\nВы поворачиваете 2 кольцо. Оно принимает вид волка.")
             colza["volk"] = 2
             zagadka(colza)
         else:    
          print("\nКольцо уже в правильном положении. Попробуйте другое.")
          zagadka(colza)
        case 3:
         print("\nТретье кольцо не двигается. Видимо, оно уже находится в верном положении.")
         zagadka(colza)
        case _:
         print("\nКажется, для Вас это слишком сложно. Вы пытались провернуть еще 1 кольцо, которого, наудивление, не существовало. \nВы возвращаетесь назад, горюя о том, что никто снова не воспринимает Вашей гениальности")
         zagadka(colza) 
 else:
   print("\nНаконец, применив все свои умственные способности, Вы решаете загадку. \nСледом, вставляете в пазы ключ-коготь. Дверь медленно открывается.")
   inventar.remove("Сапфировый коготь")
   print("\nСапфировый коготь застревает в двери. Ваш инвентарь: ",inventar)
   xoroshayakonzovka()

def xoroshayakonzovka():
  print("\n------------------------------Хорошая концовка------------------------------")
  print("\nПопав в новую, светлую комнату, Вы осматриваетесь и в ней. В глаза сразу бросается стена слов, на которой вы привычно встречаете новое драконье слово Крика. \n\"Упорство\" - гласит оно.")
  print("Кажется, именно его вам не хватало для коллекции Криков, что Вы собирали годами. Теперь, можете спокойно говорить с Патрунаксом на его языке. \nРядом стоит огромный сундук. ")
  print("В нём вы находите огромное количество самоцветов и золота, а так же - кучу других сокровищ. Кажется, стоит поделиться ими с Луканом, ведь именно он отдал вам ключ.")
  print("На этом новое приключение Довакина подходит к концу. Будоражащий опыт наводит Вас на мысль: \"Стоило бы вернуться к прежнему ремеслу...\"")
  print(f"И правда, стоит продолжить покорять вершины, великий Довакин {name}! Удачи!")
  b = input()
  exit()
def death():
  print("\n------------------------------Плохая концовка------------------------------")
  print("\nВаши веки медленно закрываются, а сердце замедляет свой ход, переставая гонять кровь. В предсмертной агонии Вы думаете о том, что все получилось бы, будь Вы немного умнее. \nВеликий Довакин смог пережить гражданскую войну и возрождение драконов.")
  print("Но сапфировое подземелье забрало его жизнь безвозвратно, а душу отправило на заслуженный покой в Совнгард.")
  b = input()
  exit()
menu(vxodvixod)


