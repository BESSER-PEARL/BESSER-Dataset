





import java.util.List;
import java.util.ArrayList;

public class rqsDsl_TAnnotation  {

    private int num;
    private int id;
    private String text;
    private String type;
    private int a;
    private int b;



    public rqsDsl_TAnnotation(
        int num,        int id,        String text,        String type,        int a,        int b    ) {
        this.num = num;
        this.id = id;
        this.text = text;
        this.type = type;
        this.a = a;
        this.b = b;
    }


    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getA() {
        return a;
    }

    public void setA(int a) {
        this.a = a;
    }
    public int getB() {
        return b;
    }

    public void setB(int b) {
        this.b = b;
    }


}