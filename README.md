# android-asset-resizer
Asset resizer for android applications. Powered by **Django**.

Live on <a href='https://android-asset-resizer.herokuapp.com/' target="_blank">https://android-asset-resizer.herokuapp.com/</a>

To be able to use the system, sign up process is required. After creating account, one can simply upload the image file(xxxhdpi based) and get the prepared assets folder for each size.

The system output is a zip file. It produces directory tree like this:     

**assets.zip**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- assets  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-ldpi  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-mdpi  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-hdpi  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-xhdpi  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-xxhddpi  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- drawable-xxxhdpi  


While generating assets, precalculated ratios are used between xxxhdpi image and the others. These ratios are like the following:
- xxxhdpi&nbsp;: 1.0000  
- xxhdpi&nbsp;&nbsp;&nbsp;: 0.7500  
- xhdpi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 0.5000  
- hdpi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 0.3750  
- mdpi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 0.2500  
- ldpi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 0.1875  
