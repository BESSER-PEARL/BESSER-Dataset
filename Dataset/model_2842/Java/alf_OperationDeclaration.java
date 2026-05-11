





import java.util.List;
import java.util.ArrayList;

public class alf_OperationDeclaration  {

    private String name;





    private alf_TypePart alf_typepart;




    private alf_RedefinitionClause alf_redefinitionclause;




    private alf_OperationDefinitionOrStub alf_operationdefinitionorstub;


    public alf_OperationDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }
    public alf_RedefinitionClause getAlf_redefinitionclause() {
        return alf_redefinitionclause;
    }

    public void setAlf_redefinitionclause(alf_RedefinitionClause alf_redefinitionclause) {
        this.alf_redefinitionclause = alf_redefinitionclause;
    }
    public alf_OperationDefinitionOrStub getAlf_operationdefinitionorstub() {
        return alf_operationdefinitionorstub;
    }

    public void setAlf_operationdefinitionorstub(alf_OperationDefinitionOrStub alf_operationdefinitionorstub) {
        this.alf_operationdefinitionorstub = alf_operationdefinitionorstub;
    }

}