





import java.util.List;
import java.util.ArrayList;

public class gast_types_TypeAlias extends types_TypeDecorator, types_Member {

    private boolean innerTypeAlias;





    private Package package;




    private GASTType gasttype;


    public gast_types_TypeAlias(
        boolean innerTypeAlias    ) {
        super(
        );
        this.innerTypeAlias = innerTypeAlias;
    }


    public boolean getInnertypealias() {
        return innerTypeAlias;
    }

    public void setInnertypealias(boolean innerTypeAlias) {
        this.innerTypeAlias = innerTypeAlias;
    }

    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }
    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }

}