





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_RepositoryReference  {

    private String location;
    private int type;
    private int options;
    private String nickname;



    public aggregator_p2_RepositoryReference(
        String location,        int type,        int options,        String nickname    ) {
        this.location = location;
        this.type = type;
        this.options = options;
        this.nickname = nickname;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public int getOptions() {
        return options;
    }

    public void setOptions(int options) {
        this.options = options;
    }
    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }


}