





import java.util.List;
import java.util.ArrayList;

public class library_CommunityRole  {

    private String role;





    private library_Community library_community;




    private library_Community library_community;




    private List<library_Writer> library_writers;




    private library_Writer library_writer;


    public library_CommunityRole(
        String role    ) {
        this.role = role;
        this.library_writers = new ArrayList<>();
    }

    public library_CommunityRole(
        String role        ArrayList<library_Writer> library_writers    ) {
        this.role = role;
        this.library_writers = library_writers;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public library_Community getLibrary_community() {
        return library_community;
    }

    public void setLibrary_community(library_Community library_community) {
        this.library_community = library_community;
    }
    public library_Community getLibrary_community() {
        return library_community;
    }

    public void setLibrary_community(library_Community library_community) {
        this.library_community = library_community;
    }
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}