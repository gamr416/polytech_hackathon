MAIN_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="windowModality">
   <enum>Qt::WindowModal</enum>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1065</width>
    <height>816</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Переводчик сленга</string>
  </property>
  <property name="styleSheet">
   <string notr="true">#centralwidget {
 background-color: rgb(0, 0, 0);
}
QPushButton {
 background-color: rgb(29, 32, 30);
 border-radius: 10px;
 padding: 10px 10px;
 color: rgb(246, 255, 248);
border: 1px  solid rgb(65, 205, 82);
}
QPushButton:hover {
background-color: rgb(29, 32, 30);
 color: rgb(65, 205, 82);
 border: 2px  solid rgb(65, 205, 82);
}

QLineEdit {
background-color: rgb(29, 32, 30);
 padding: 30px;
 border-radius:5px;
 color: rgb(246, 255, 248);
}
QTextBrowser{
background-color: rgb(29, 32, 30);
 border-radius: 10px;
 padding: 10px 10px;
 color: rgb(246, 255, 248);
}

QRadioButton{
 color: rgb(246, 255, 248);
}

QRadioButton:indicator{
width: 20px;
height: 20px;
}
QRadioButton:indicator:unchecked{
background-color: rgb(92, 92, 92);
}
QRadioButton:indicator:checked{
background-color: rgb(65, 205, 82);
}</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <spacer name="horizontalSpacer">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>40</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QPushButton" name="dictionary_button">
        <property name="font">
         <font>
          <pointsize>15</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="text">
         <string>Перейти к словарю</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QLineEdit" name="main_text_edit">
      <property name="font">
       <font>
        <pointsize>20</pointsize>
       </font>
      </property>
      <property name="text">
       <string/>
      </property>
      <property name="frame">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QPushButton" name="dict_search">
        <property name="font">
         <font>
          <pointsize>20</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="text">
         <string>Перевести</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QRadioButton" name="word_button">
          <property name="font">
           <font>
            <pointsize>20</pointsize>
           </font>
          </property>
          <property name="styleSheet">
           <string notr="true">QRRadioButton {
	color:  rgb(255, 255, 255);
}</string>
          </property>
          <property name="text">
           <string>Слово</string>
          </property>
          <property name="checked">
           <bool>false</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QRadioButton" name="sentence_button">
          <property name="font">
           <font>
            <pointsize>20</pointsize>
           </font>
          </property>
          <property name="text">
           <string>Предложение</string>
          </property>
          <property name="checked">
           <bool>true</bool>
          </property>
          <property name="autoRepeat">
           <bool>false</bool>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QTextBrowser" name="translated_text">
      <property name="font">
       <font>
        <pointsize>24</pointsize>
       </font>
      </property>
      <property name="html">
       <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Noto Sans'; font-size:13pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="images/test.qrc"/>
 </resources>
 <connections/>
</ui>

"""