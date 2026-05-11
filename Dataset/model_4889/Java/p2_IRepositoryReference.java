





import java.util.List;
import java.util.ArrayList;

public class p2_IRepositoryReference  {

    private int options;
    private String location;
    private String nickname;
    private int type;



    public p2_IRepositoryReference(
        int options,        String location,        String nickname,        int type    ) {
        this.options = options;
        this.location = location;
        this.nickname = nickname;
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


}