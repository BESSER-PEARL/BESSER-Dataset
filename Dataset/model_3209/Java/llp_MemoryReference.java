





import java.util.List;
import java.util.ArrayList;

public class llp_MemoryReference  {

    private String address;





    private llp_IOInstruction llp_ioinstruction;




    private llp_SynchronisationInstruction llp_synchronisationinstruction;


    public llp_MemoryReference(
        String address    ) {
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public llp_IOInstruction getLlp_ioinstruction() {
        return llp_ioinstruction;
    }

    public void setLlp_ioinstruction(llp_IOInstruction llp_ioinstruction) {
        this.llp_ioinstruction = llp_ioinstruction;
    }
    public llp_SynchronisationInstruction getLlp_synchronisationinstruction() {
        return llp_synchronisationinstruction;
    }

    public void setLlp_synchronisationinstruction(llp_SynchronisationInstruction llp_synchronisationinstruction) {
        this.llp_synchronisationinstruction = llp_synchronisationinstruction;
    }

}