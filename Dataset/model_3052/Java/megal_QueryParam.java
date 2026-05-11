





import java.util.List;
import java.util.ArrayList;

public class megal_QueryParam extends QueryEntry {

    private String name;





    private megal_MegalEntityType megal_megalentitytype;


    public megal_QueryParam(
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

    public megal_MegalEntityType getMegal_megalentitytype() {
        return megal_megalentitytype;
    }

    public void setMegal_megalentitytype(megal_MegalEntityType megal_megalentitytype) {
        this.megal_megalentitytype = megal_megalentitytype;
    }

}