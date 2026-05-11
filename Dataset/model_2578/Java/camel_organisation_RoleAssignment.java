




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_organisation_RoleAssignment  {

    private LocalDate startTime;
    private String name;
    private LocalDate assignmentTime;
    private LocalDate endTime;





    private User user;




    private UserGroup usergroup;




    private Role role;


    public camel_organisation_RoleAssignment(
        LocalDate startTime,        String name,        LocalDate assignmentTime,        LocalDate endTime    ) {
        this.startTime = startTime;
        this.name = name;
        this.assignmentTime = assignmentTime;
        this.endTime = endTime;
    }


    public LocalDate getStarttime() {
        return startTime;
    }

    public void setStarttime(LocalDate startTime) {
        this.startTime = startTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getAssignmenttime() {
        return assignmentTime;
    }

    public void setAssignmenttime(LocalDate assignmentTime) {
        this.assignmentTime = assignmentTime;
    }
    public LocalDate getEndtime() {
        return endTime;
    }

    public void setEndtime(LocalDate endTime) {
        this.endTime = endTime;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public UserGroup getUsergroup() {
        return usergroup;
    }

    public void setUsergroup(UserGroup usergroup) {
        this.usergroup = usergroup;
    }
    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

}