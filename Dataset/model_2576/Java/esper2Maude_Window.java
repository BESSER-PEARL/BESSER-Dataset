





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_Window  {

    private String typeBatch;
    private String typeTime;
    private int num;



    public esper2Maude_Window(
        String typeBatch,        String typeTime,        int num    ) {
        this.typeBatch = typeBatch;
        this.typeTime = typeTime;
        this.num = num;
    }


    public String getTypebatch() {
        return typeBatch;
    }

    public void setTypebatch(String typeBatch) {
        this.typeBatch = typeBatch;
    }
    public String getTypetime() {
        return typeTime;
    }

    public void setTypetime(String typeTime) {
        this.typeTime = typeTime;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }


}