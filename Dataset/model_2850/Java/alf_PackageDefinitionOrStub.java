





import java.util.List;
import java.util.ArrayList;

public class alf_PackageDefinitionOrStub extends PackagedElementDefinition {






    private alf_PackageDeclaration alf_packagedeclaration;




    private alf_PackageBody alf_packagebody;


    public alf_PackageDefinitionOrStub(
    ) {
        super(
        );
    }



    public alf_PackageDeclaration getAlf_packagedeclaration() {
        return alf_packagedeclaration;
    }

    public void setAlf_packagedeclaration(alf_PackageDeclaration alf_packagedeclaration) {
        this.alf_packagedeclaration = alf_packagedeclaration;
    }
    public alf_PackageBody getAlf_packagebody() {
        return alf_packagebody;
    }

    public void setAlf_packagebody(alf_PackageBody alf_packagebody) {
        this.alf_packagebody = alf_packagebody;
    }

}