





import java.util.List;
import java.util.ArrayList;

public class dsl_SlackPUT extends Action {

    private String team;
    private String value;
    private String channel;



    public dsl_SlackPUT(
        String team,        String value,        String channel    ) {
        super(
        );
        this.team = team;
        this.value = value;
        this.channel = channel;
    }


    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
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


}