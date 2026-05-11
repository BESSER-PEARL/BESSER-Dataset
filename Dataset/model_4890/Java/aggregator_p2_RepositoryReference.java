





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_RepositoryReference  {

    private String location;
    private String nickname;
    private int options;
    private int type;



    public aggregator_p2_RepositoryReference(
        String location,        String nickname,        int options,        int type    ) {
        this.location = location;
        this.nickname = nickname;
        this.options = options;
        this.type = type;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
    public int getOptions() {
        return options;
    }

    public void setOptions(int options) {
        this.options = options;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }


}