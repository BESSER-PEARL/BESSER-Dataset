





import java.util.List;
import java.util.ArrayList;

public class p2_ITouchpointInstruction  {

    private String body;
    private String importAttribute;





    private p2_InstructionMap p2_instructionmap;


    public p2_ITouchpointInstruction(
        String body,        String importAttribute    ) {
        this.body = body;
        this.importAttribute = importAttribute;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getImportattribute() {
        return importAttribute;
    }

    public void setImportattribute(String importAttribute) {
        this.importAttribute = importAttribute;
    }

    public p2_InstructionMap getP2_instructionmap() {
        return p2_instructionmap;
    }

    public void setP2_instructionmap(p2_InstructionMap p2_instructionmap) {
        this.p2_instructionmap = p2_instructionmap;
    }

}