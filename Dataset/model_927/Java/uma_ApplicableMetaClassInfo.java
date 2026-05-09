





import java.util.List;
import java.util.ArrayList;

public class uma_ApplicableMetaClassInfo extends Classifier {

    private String isPrimaryExtension;





    private uma_Kind uma_kind;


    public uma_ApplicableMetaClassInfo(
        String isPrimaryExtension    ) {
        super(
        );
        this.isPrimaryExtension = isPrimaryExtension;
    }


    public String getIsprimaryextension() {
        return isPrimaryExtension;
    }

    public void setIsprimaryextension(String isPrimaryExtension) {
        this.isPrimaryExtension = isPrimaryExtension;
    }

    public uma_Kind getUma_kind() {
        return uma_kind;
    }

    public void setUma_kind(uma_Kind uma_kind) {
        this.uma_kind = uma_kind;
    }

}