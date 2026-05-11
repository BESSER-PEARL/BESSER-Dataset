





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_FilterPart  {

    private String eventVariable;
    private int num;
    private String neg;
    private String str;
    private int dec;
    private String t;
    private String f;
    private String eventPropName;





    private esper2Maude_FilterEvent esper2maude_filterevent;




    private esper2Maude_FilterEvent esper2maude_filterevent;


    public esper2Maude_FilterPart(
        String eventVariable,        int num,        String neg,        String str,        int dec,        String t,        String f,        String eventPropName    ) {
        this.eventVariable = eventVariable;
        this.num = num;
        this.neg = neg;
        this.str = str;
        this.dec = dec;
        this.t = t;
        this.f = f;
        this.eventPropName = eventPropName;
    }


    public String getEventvariable() {
        return eventVariable;
    }

    public void setEventvariable(String eventVariable) {
        this.eventVariable = eventVariable;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public String getNeg() {
        return neg;
    }

    public void setNeg(String neg) {
        this.neg = neg;
    }
    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }
    public int getDec() {
        return dec;
    }

    public void setDec(int dec) {
        this.dec = dec;
    }
    public String getT() {
        return t;
    }

    public void setT(String t) {
        this.t = t;
    }
    public String getF() {
        return f;
    }

    public void setF(String f) {
        this.f = f;
    }
    public String getEventpropname() {
        return eventPropName;
    }

    public void setEventpropname(String eventPropName) {
        this.eventPropName = eventPropName;
    }

    public esper2Maude_FilterEvent getEsper2maude_filterevent() {
        return esper2maude_filterevent;
    }

    public void setEsper2maude_filterevent(esper2Maude_FilterEvent esper2maude_filterevent) {
        this.esper2maude_filterevent = esper2maude_filterevent;
    }
    public esper2Maude_FilterEvent getEsper2maude_filterevent() {
        return esper2maude_filterevent;
    }

    public void setEsper2maude_filterevent(esper2Maude_FilterEvent esper2maude_filterevent) {
        this.esper2maude_filterevent = esper2maude_filterevent;
    }

}