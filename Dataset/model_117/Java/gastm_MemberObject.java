





import java.util.List;
import java.util.ArrayList;

public class gastm_MemberObject extends MinorSyntaxObject {

    private String offset;





    private gastm_DefinitionObject gastm_definitionobject;


    public gastm_MemberObject(
        String offset    ) {
        super(
        );
        this.offset = offset;
    }


    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }

    public gastm_DefinitionObject getGastm_definitionobject() {
        return gastm_definitionobject;
    }

    public void setGastm_definitionobject(gastm_DefinitionObject gastm_definitionobject) {
        this.gastm_definitionobject = gastm_definitionobject;
    }

}