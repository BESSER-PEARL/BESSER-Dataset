





import java.util.List;
import java.util.ArrayList;

public class imdb_User  {

    private String watchlist;
    private String username;





    private imdb_StaffList imdb_stafflist;


    public imdb_User(
        String watchlist,        String username    ) {
        this.watchlist = watchlist;
        this.username = username;
    }


    public String getWatchlist() {
        return watchlist;
    }

    public void setWatchlist(String watchlist) {
        this.watchlist = watchlist;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public imdb_StaffList getImdb_stafflist() {
        return imdb_stafflist;
    }

    public void setImdb_stafflist(imdb_StaffList imdb_stafflist) {
        this.imdb_stafflist = imdb_stafflist;
    }

}