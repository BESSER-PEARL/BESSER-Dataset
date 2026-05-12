





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_RepositoryReference  {

    private int options;
    private String nickname;
    private int type;
    private String location;



    public aggregator_p2_RepositoryReference(
        int options,        String nickname,        int type,        String location    ) {
        this.options = options;
        this.nickname = nickname;
        this.type = type;
        this.location = location;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}