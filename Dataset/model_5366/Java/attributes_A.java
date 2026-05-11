





import java.util.List;
import java.util.ArrayList;

public class attributes_A  {

    private String comment;
    private String b;
    private String c;
    private String d;
    private String id;
    private String name;



    public attributes_A(
        String comment,        String b,        String c,        String d,        String id,        String name    ) {
        this.comment = comment;
        this.b = b;
        this.c = c;
        this.d = d;
        this.id = id;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }
    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }
    public String getD() {
        return d;
    }

    public void setD(String d) {
        this.d = d;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}