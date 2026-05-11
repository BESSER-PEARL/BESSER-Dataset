





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_RepositoryReference  {

    private String nickname;
    private int type;
    private int options;
    private String location;



    public aggregator_p2_RepositoryReference(
        String nickname,        int type,        int options,        String location    ) {
        this.nickname = nickname;
        this.type = type;
        this.options = options;
        this.location = location;
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
    public int getOptions() {
        return options;
    }

    public void setOptions(int options) {
        this.options = options;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}