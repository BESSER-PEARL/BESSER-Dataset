





import java.util.List;
import java.util.ArrayList;

public class uppaal_declarations_ChannelVariableDeclaration extends VariableDeclaration {

    private boolean urgent;
    private boolean broadcast;



    public uppaal_declarations_ChannelVariableDeclaration(
        boolean urgent,        boolean broadcast    ) {
        super(
        );
        this.urgent = urgent;
        this.broadcast = broadcast;
    }


    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }
    public boolean getBroadcast() {
        return broadcast;
    }

    public void setBroadcast(boolean broadcast) {
        this.broadcast = broadcast;
    }


}