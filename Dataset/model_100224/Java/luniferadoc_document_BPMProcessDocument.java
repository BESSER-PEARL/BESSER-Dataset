





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_document_BPMProcessDocument extends LuniferaDocDocument {

    private String process;



    public luniferadoc_document_BPMProcessDocument(
        String process    ) {
        super(
        );
        this.process = process;
    }


    public String getProcess() {
        return process;
    }

    public void setProcess(String process) {
        this.process = process;
    }


}