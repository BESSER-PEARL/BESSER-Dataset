





import java.util.List;
import java.util.ArrayList;

public class mitra_VarDeclaration  {

    private String name;





    private mitra_Type mitra_type;


    public mitra_VarDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mitra_Type getMitra_type() {
        return mitra_type;
    }

    public void setMitra_type(mitra_Type mitra_type) {
        this.mitra_type = mitra_type;
    }

}