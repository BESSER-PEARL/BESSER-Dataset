





import java.util.List;
import java.util.ArrayList;

public class td1_Trigger  {

    private String codeFiacre;
    private int ArgSize;
    private String Body;
    private String Name;



    public td1_Trigger(
        String codeFiacre,        int ArgSize,        String Body,        String Name    ) {
        this.codeFiacre = codeFiacre;
        this.ArgSize = ArgSize;
        this.Body = Body;
        this.Name = Name;
    }


    public String getCodefiacre() {
        return codeFiacre;
    }

    public void setCodefiacre(String codeFiacre) {
        this.codeFiacre = codeFiacre;
    }
    public int getArgsize() {
        return ArgSize;
    }

    public void setArgsize(int ArgSize) {
        this.ArgSize = ArgSize;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}