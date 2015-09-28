from tkinter import *
from tkinter import ttk
import module1
from geopy import geocoders # $ pip  install geopy
import calendar
from datetime import datetime
import pytz # $ pip install pytz

class time:
      def __init__(self,master):
            self.frame = Tk.frame(master) 
            master.configure(background = '#e1d8b9')
            self.style = ttk.Style()
            self.style.configure('TButton',  background = 'black' , font=("Arial", 12,"bold"))   
            label = ttk.Label(master, text = "Choose your country: ",background = '#e1d8b9', font=('Arial',13,'bold')).grid(row = 0, column =0, padx = 100,pady=20 ,sticky = 'sw')
            countries = StringVar()
            self.combobox_countries = ttk.Combobox(master, width = 40, height= 10,textvariable = countries, justify = CENTER )
            self.combobox_countries.grid(row = 1 , column =0, padx = 100)
            self.combobox_countries.config( values = ('Afghanistan','Albania','Algeria','American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua And Barbuda','Argentina','Armenia','Aruba','Australia','Austria',
                            'Azerbaijan','Bahamas','Bahrain','Bangladesh',
                            'Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia',
                            'Bosnia And Herzegovina','Botswana','Bouvet Island','Brazil','British Indian Ocean Territory','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Cayman Islands','Central African Republic',
                            'Chad','Chile','China','Christmas Island',
                            'Cocos (Keeling) Islands','Columbia','Comoros','Congo',
                            'Cook Islands','Costa Rica','Cote D\'Ivorie (Ivory Coast)',
                            'Croatia (Hrvatska)','Cuba','Cyprus','Czech Republic','Democratic Republic Of Congo (Zaire)','Denmark',
                            'Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt',
                            'El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Falkland Islands (Malvinas)',
                            'Faroe Islands','Fiji','Finland','France','France, Metropolitan',
                            'French Guinea','French Polynesia','French Southern Territories','Gabon',
                            'Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guadeloupe','Guam',
                            'Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti',
                            'Heard And McDonald Islands','Honduras','Hong Kong','Hungary','Iceland',
                            'India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan',
                            'Kenya','Kiribati','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali',
                            'Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montserrat','Morocco','Mozambique','Myanmar (Burma)','Namibia','Nauru','Nepal','Netherlands','Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','North Korea','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay',
                            'Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russia','Rwanda','Saint Helena','Saint Kitts And Nevis','Saint Lucia','Saint Pierre And Miquelon','Saint Vincent And The Grenadines','San Marino','Sao Tome And Principe',
                            'Saudi Arabia','Senegal','Seychelles','Sierra Leone','Singapore','Slovak Republic','Slovenia','Solomon Islands',
                            'Somalia','South Africa','South Georgia And South Sandwich Islands','South Korea','Spain','Sri Lanka','Sudan','Suriname','Svalbard And Jan Mayen','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania',
                            'Thailand','Togo','Tokelau','Tonga','Trinidad And Tobago','Tunisia','Turkey','Turkmenistan','Turks And Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','United States Minor Outlying Islands','Uruguay','Uzbekistan','Vanuatu','Vatican City (Holy See)','Venezuela','Vietnam','Virgin Islands (British)','Virgin Islands (US)','Wallis And Futuna Islands','Western Sahara','Western Samoa','Yemen','Yugoslavia','Zambia','Zimbabwe'))
            label = ttk.Label(master, text = "Type in your city: ",background = '#e1d8b9', font=('Arial',13,'bold')).grid(row = 0, column = 1, padx = 100, pady = 20, sticky = 'sw')
            cities = StringVar()
            self.combobox_cities = ttk.Entry( master , width = 40, textvariable = cities)
            self.combobox_cities.grid(row = 1 , column= 1, padx = 100)
            button = ttk.Button(master,style='TButton', text = "Check the time", command = self.Checktime)
            button.grid(row = 2, column =0,columnspan=2, pady= 50, padx = 385, sticky = 'ne' )
            self.Entry_comments =Text(master , width = 40 ,height = 9,font=('Arial',12))
            self.Entry_comments.grid(row = 3, column =0, columnspan=2, padx=160)
      def Checktime(self):
           country = self.combobox_countries.get()
           cities = self.combobox_cities.get()
           module1.hours(cities)
      
                
          
def main():
    root = Tk()

    app = time(root)
    root.mainloop()

if __name__=="__main__":main()