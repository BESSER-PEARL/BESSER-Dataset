





import java.util.List;
import java.util.ArrayList;

public class megal_MegalFile extends MegalElement {

    private String name;





    private megal_MegalFile megal_megalfile;


    public megal_MegalFile(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public megal_MegalFile getMegal_megalfile() {
        return megal_megalfile;
    }

    public void setMegal_megalfile(megal_MegalFile megal_megalfile) {
        this.megal_megalfile = megal_megalfile;
    }

}