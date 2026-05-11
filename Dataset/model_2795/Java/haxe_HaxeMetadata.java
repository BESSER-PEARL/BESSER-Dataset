





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeMetadata extends HaxeExpression, HaxeNamedElement {

    private boolean compilerMetadata;





    private haxe_HaxeMetadataContainer haxe_haxemetadatacontainer;




    private List<haxe_HaxeExpression> haxe_haxeexpressions;




    private haxe_HaxeMetadataContainer haxe_haxemetadatacontainer;


    public haxe_HaxeMetadata(
        boolean compilerMetadata    ) {
        super(
        );
        this.compilerMetadata = compilerMetadata;
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeMetadata(
        boolean compilerMetadata        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.compilerMetadata = compilerMetadata;
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }

    public boolean getCompilermetadata() {
        return compilerMetadata;
    }

    public void setCompilermetadata(boolean compilerMetadata) {
        this.compilerMetadata = compilerMetadata;
    }

    public haxe_HaxeMetadataContainer getHaxe_haxemetadatacontainer() {
        return haxe_haxemetadatacontainer;
    }

    public void setHaxe_haxemetadatacontainer(haxe_HaxeMetadataContainer haxe_haxemetadatacontainer) {
        this.haxe_haxemetadatacontainer = haxe_haxemetadatacontainer;
    }
    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }
    public haxe_HaxeMetadataContainer getHaxe_haxemetadatacontainer() {
        return haxe_haxemetadatacontainer;
    }

    public void setHaxe_haxemetadatacontainer(haxe_HaxeMetadataContainer haxe_haxemetadatacontainer) {
        this.haxe_haxemetadatacontainer = haxe_haxemetadatacontainer;
    }

}