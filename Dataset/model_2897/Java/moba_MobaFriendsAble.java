





import java.util.List;
import java.util.ArrayList;

public class moba_MobaFriendsAble extends MobaPropertiesAble {






    private List<moba_MobaFriend> moba_mobafriends;


    public moba_MobaFriendsAble(
    ) {
        super(
        );
        this.moba_mobafriends = new ArrayList<>();
    }

    public moba_MobaFriendsAble(
        ArrayList<moba_MobaFriend> moba_mobafriends    ) {
        this.moba_mobafriends = moba_mobafriends;
    }


    public List<moba_MobaFriend> getMoba_mobafriends() {
        return moba_mobafriends;
    }

    public void addMoba_mobafriend(Moba_mobafriend moba_mobafriend) {
        this.moba_mobafriends.add(moba_mobafriend);
    }

}