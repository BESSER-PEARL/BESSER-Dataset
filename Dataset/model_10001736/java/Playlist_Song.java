





import java.util.List;
import java.util.ArrayList;

public class Playlist_Song  {

    private int sID;
    private int pID;





    private Song song;




    private Playlist playlist;


    public Playlist_Song(
        int sID,        int pID    ) {
        this.sID = sID;
        this.pID = pID;
    }


    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }
    public int getPid() {
        return pID;
    }

    public void setPid(int pID) {
        this.pID = pID;
    }

    public Song getSong() {
        return song;
    }

    public void setSong(Song song) {
        this.song = song;
    }
    public Playlist getPlaylist() {
        return playlist;
    }

    public void setPlaylist(Playlist playlist) {
        this.playlist = playlist;
    }

}