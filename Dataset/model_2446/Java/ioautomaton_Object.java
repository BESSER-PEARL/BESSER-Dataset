





import java.util.List;
import java.util.ArrayList;

public class ioautomaton_Object  {

    private String name;





    private ioautomaton_OutMessage ioautomaton_outmessage;


    public ioautomaton_Object(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioautomaton_OutMessage getIoautomaton_outmessage() {
        return ioautomaton_outmessage;
    }

    public void setIoautomaton_outmessage(ioautomaton_OutMessage ioautomaton_outmessage) {
        this.ioautomaton_outmessage = ioautomaton_outmessage;
    }

}