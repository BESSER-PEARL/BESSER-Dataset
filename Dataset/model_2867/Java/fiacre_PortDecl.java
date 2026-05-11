





import java.util.List;
import java.util.ArrayList;

public class fiacre_PortDecl  {

    private boolean in_;
    private boolean out;
    private String name;





    private fiacre_Priority fiacre_priority;




    private fiacre_Priority fiacre_priority;




    private fiacre_Channel fiacre_channel;


    public fiacre_PortDecl(
        boolean in_,        boolean out,        String name    ) {
        this.in_ = in_;
        this.out = out;
        this.name = name;
    }


    public boolean getIn_() {
        return in_;
    }

    public void setIn_(boolean in_) {
        this.in_ = in_;
    }
    public boolean getOut() {
        return out;
    }

    public void setOut(boolean out) {
        this.out = out;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_Priority getFiacre_priority() {
        return fiacre_priority;
    }

    public void setFiacre_priority(fiacre_Priority fiacre_priority) {
        this.fiacre_priority = fiacre_priority;
    }
    public fiacre_Priority getFiacre_priority() {
        return fiacre_priority;
    }

    public void setFiacre_priority(fiacre_Priority fiacre_priority) {
        this.fiacre_priority = fiacre_priority;
    }
    public fiacre_Channel getFiacre_channel() {
        return fiacre_channel;
    }

    public void setFiacre_channel(fiacre_Channel fiacre_channel) {
        this.fiacre_channel = fiacre_channel;
    }

}