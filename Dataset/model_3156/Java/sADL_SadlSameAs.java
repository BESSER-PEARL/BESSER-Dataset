





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlSameAs extends SadlStatement {

    private boolean complement;





    private sADL_SadlResource sadl_sadlresource;


    public sADL_SadlSameAs(
        boolean complement    ) {
        super(
        );
        this.complement = complement;
    }


    public boolean getComplement() {
        return complement;
    }

    public void setComplement(boolean complement) {
        this.complement = complement;
    }

    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }

}