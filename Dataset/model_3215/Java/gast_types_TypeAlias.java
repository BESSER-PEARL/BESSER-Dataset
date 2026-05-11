





import java.util.List;
import java.util.ArrayList;

public class gast_types_TypeAlias extends types_Member, types_TypeDecorator {

    private boolean innerTypeAlias;





    private GASTType gasttype;




    private Package package;




    private GASTClass gastclass;


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

    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }

}