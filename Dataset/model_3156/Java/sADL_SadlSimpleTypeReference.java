





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlSimpleTypeReference extends SadlTypeReference {

    private boolean list;





    private sADL_SadlResource sadl_sadlresource;


    public sADL_SadlSimpleTypeReference(
        boolean list    ) {
        super(
        );
        this.list = list;
    }


    public boolean getList() {
        return list;
    }

    public void setList(boolean list) {
        this.list = list;
    }

    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }

}