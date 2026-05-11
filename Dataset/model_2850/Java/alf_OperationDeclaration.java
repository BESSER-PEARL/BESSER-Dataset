





import java.util.List;
import java.util.ArrayList;

public class alf_OperationDeclaration extends OperationDefinitionOrStub {

    private boolean isAbstract;





    private alf_FormalParameters alf_formalparameters;




    private alf_TypePart alf_typepart;




    private alf_Name alf_name;




    private alf_Block alf_block;


    public alf_OperationDeclaration(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_FormalParameters getAlf_formalparameters() {
        return alf_formalparameters;
    }

    public void setAlf_formalparameters(alf_FormalParameters alf_formalparameters) {
        this.alf_formalparameters = alf_formalparameters;
    }
    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }
    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }
    public alf_Block getAlf_block() {
        return alf_block;
    }

    public void setAlf_block(alf_Block alf_block) {
        this.alf_block = alf_block;
    }

}