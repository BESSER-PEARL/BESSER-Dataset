





import java.util.List;
import java.util.ArrayList;

public class list_VersionedList extends ProductSpaceElement {






    private List<list_VersionedListVertex> list_versionedlistvertexs;




    private list_VersionedListVertex list_versionedlistvertex;




    private List<list_VersionedListEdge> list_versionedlistedges;




    private list_VersionedListEdge list_versionedlistedge;




    private list_VersionedListStartReference list_versionedliststartreference;




    private List<list_VersionedListStartReference> list_versionedliststartreferences;


    public list_VersionedList(
    ) {
        super(
        );
        this.list_versionedlistvertexs = new ArrayList<>();
        this.list_versionedlistedges = new ArrayList<>();
        this.list_versionedliststartreferences = new ArrayList<>();
    }

    public list_VersionedList(
        ArrayList<list_VersionedListVertex> list_versionedlistvertexs,        ArrayList<list_VersionedListEdge> list_versionedlistedges,        ArrayList<list_VersionedListStartReference> list_versionedliststartreferences    ) {
        this.list_versionedlistvertexs = list_versionedlistvertexs;
        this.list_versionedlistedges = list_versionedlistedges;
        this.list_versionedliststartreferences = list_versionedliststartreferences;
    }


    public List<list_VersionedListVertex> getList_versionedlistvertexs() {
        return list_versionedlistvertexs;
    }

    public void addList_versionedlistvertex(List_versionedlistvertex list_versionedlistvertex) {
        this.list_versionedlistvertexs.add(list_versionedlistvertex);
    }
    public list_VersionedListVertex getList_versionedlistvertex() {
        return list_versionedlistvertex;
    }

    public void setList_versionedlistvertex(list_VersionedListVertex list_versionedlistvertex) {
        this.list_versionedlistvertex = list_versionedlistvertex;
    }
    public List<list_VersionedListEdge> getList_versionedlistedges() {
        return list_versionedlistedges;
    }

    public void addList_versionedlistedge(List_versionedlistedge list_versionedlistedge) {
        this.list_versionedlistedges.add(list_versionedlistedge);
    }
    public list_VersionedListEdge getList_versionedlistedge() {
        return list_versionedlistedge;
    }

    public void setList_versionedlistedge(list_VersionedListEdge list_versionedlistedge) {
        this.list_versionedlistedge = list_versionedlistedge;
    }
    public list_VersionedListStartReference getList_versionedliststartreference() {
        return list_versionedliststartreference;
    }

    public void setList_versionedliststartreference(list_VersionedListStartReference list_versionedliststartreference) {
        this.list_versionedliststartreference = list_versionedliststartreference;
    }
    public List<list_VersionedListStartReference> getList_versionedliststartreferences() {
        return list_versionedliststartreferences;
    }

    public void addList_versionedliststartreference(List_versionedliststartreference list_versionedliststartreference) {
        this.list_versionedliststartreferences.add(list_versionedliststartreference);
    }

}