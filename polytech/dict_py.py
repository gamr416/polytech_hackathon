DICT_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>widget</class>
 <widget class="QWidget" name="widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>700</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>700</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Словарь</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>../img/image.png</normaloff>../img/image.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">#centralwidget {
 background-color: rgb(0, 0, 0);
}

QTextBrowser{
background-color: rgb(29, 32, 30);
 border-radius: 10px;
 padding: 10px 10px;
 color: rgb(246, 255, 248);
}</string>
  </property>
  <layout class="QHBoxLayout" name="horizontalLayout">
   <item>
    <widget class="QTextBrowser" name="main_dict">
     <property name="font">
      <font>
       <family>Noto Sans Mono</family>
       <pointsize>13</pointsize>
      </font>
     </property>
     <property name="html">
      <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Noto Sans Mono'; font-size:13pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>

"""