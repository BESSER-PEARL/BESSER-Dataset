





import java.util.List;
import java.util.ArrayList;

public class sparrow_SlackPUT extends Action {

    private String value;
    private String channel;
    private String team;



    public sparrow_SlackPUT(
        String value,        String channel,        String team    ) {
        super(
        );
        this.value = value;
        this.channel = channel;
        this.team = team;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getChannel() {
        return channel;
    }

    public void setChannel(String channel) {
        this.channel = channel;
    }
    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
    }


}