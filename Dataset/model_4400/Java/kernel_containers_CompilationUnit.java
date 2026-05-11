





import java.util.List;
import java.util.ArrayList;

public class kernel_containers_CompilationUnit extends KernelRoot {






    private Start start;




    private End end;




    private List<Member> members;


    public kernel_containers_CompilationUnit(
    ) {
        super(
        );
        this.members = new ArrayList<>();
    }

    public kernel_containers_CompilationUnit(
        ArrayList<Member> members    ) {
        this.members = members;
    }


    public Start getStart() {
        return start;
    }

    public void setStart(Start start) {
        this.start = start;
    }
    public End getEnd() {
        return end;
    }

    public void setEnd(End end) {
        this.end = end;
    }
    public List<Member> getMembers() {
        return members;
    }

    public void addMember(Member member) {
        this.members.add(member);
    }

}