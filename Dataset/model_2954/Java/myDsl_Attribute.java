





import java.util.List;
import java.util.ArrayList;

public class myDsl_Attribute extends Type {

    private boolean many;





    private myDsl_Type mydsl_type;


    public myDsl_Attribute(
        boolean many    ) {
        super(
        );
        this.many = many;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}