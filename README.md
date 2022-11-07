#include&amp;lt;stdio.h&amp;gt;
#include&amp;lt;stdlib.h&amp;gt;
int main()
{
int n,i,k,flag=0;
char vari[15],typ[15],b[15],c;
printf(&amp;quot;Enter the number of variables:&amp;quot;);
scanf(&amp;quot; %d&amp;quot;,&amp;amp;n);
for(i=0;i&amp;lt;n;i++)

{
printf(&amp;quot;Enter the variable[%d]:&amp;quot;,i);
scanf(&amp;quot; %c&amp;quot;,&amp;amp;vari[i]);
printf(&amp;quot;Enter the variable-type[%d](float-f,int-i):&amp;quot;,i);
scanf(&amp;quot; %c&amp;quot;,&amp;amp;typ[i]);
if(typ[i]==&amp;#39;f&amp;#39)
flag=1;
}
printf(&amp;quot;Enter the Expression(end with $):&amp;quot;);
i=0;
getchar();
while((c=getchar())!=&amp;#39;$&amp;#39)
{
b[i]=c;
i++; }

k=i;
for(i=0;i&amp;lt;k;i++)
{
if(b[i]==&amp;#39;/&amp;#39)
{
flag=1;
break; } }
for(i=0;i&amp;lt;n;i++)

{
if(b[0]==vari[i])
{
if(flag==1)
{
if(typ[i]==&amp;#39;f&amp;#39)
{ printf(&amp;quot;\nthe datatype is correctly defined..!\n&amp;quot;);
break; }
else
{ printf(&amp;quot;Identifier %c must be a float type..!\n&amp;quot;,vari[i]);
break; } }
else
{ printf(&amp;quot;\nthe datatype is correctly defined..!\n&amp;quot;);
break; } }
}
return 0;
}
