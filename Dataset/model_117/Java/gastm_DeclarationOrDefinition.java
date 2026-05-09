





import java.util.List;
import java.util.ArrayList;

public class gastm_DeclarationOrDefinition extends DefinitionObject {

    private String linkageSpecifier;





    private gastm_StorageSpecification gastm_storagespecification;




    private gastm_AccessKind gastm_accesskind;


    public gastm_DeclarationOrDefinition(
        String linkageSpecifier    ) {
        super(
        );
        this.linkageSpecifier = linkageSpecifier;
    }


    public String getLinkagespecifier() {
        return linkageSpecifier;
    }

    public void setLinkagespecifier(String linkageSpecifier) {
        this.linkageSpecifier = linkageSpecifier;
    }

    public gastm_StorageSpecification getGastm_storagespecification() {
        return gastm_storagespecification;
    }

    public void setGastm_storagespecification(gastm_StorageSpecification gastm_storagespecification) {
        this.gastm_storagespecification = gastm_storagespecification;
    }
    public gastm_AccessKind getGastm_accesskind() {
        return gastm_accesskind;
    }

    public void setGastm_accesskind(gastm_AccessKind gastm_accesskind) {
        this.gastm_accesskind = gastm_accesskind;
    }

}