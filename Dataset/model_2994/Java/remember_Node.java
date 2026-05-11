




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class remember_Node  {

    private String description;
    private LocalDate dateModified;
    private String nodeType;
    private boolean markedForDeletion;
    private String nodeId;
    private String name;
    private LocalDate dateCreated;
    private int sequence;
    private String parentNodeType;
    private String parentNodeId;



    public remember_Node(
        String description,        LocalDate dateModified,        String nodeType,        boolean markedForDeletion,        String nodeId,        String name,        LocalDate dateCreated,        int sequence,        String parentNodeType,        String parentNodeId    ) {
        this.description = description;
        this.dateModified = dateModified;
        this.nodeType = nodeType;
        this.markedForDeletion = markedForDeletion;
        this.nodeId = nodeId;
        this.name = name;
        this.dateCreated = dateCreated;
        this.sequence = sequence;
        this.parentNodeType = parentNodeType;
        this.parentNodeId = parentNodeId;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getDatemodified() {
        return dateModified;
    }

    public void setDatemodified(LocalDate dateModified) {
        this.dateModified = dateModified;
    }
    public String getNodetype() {
        return nodeType;
    }

    public void setNodetype(String nodeType) {
        this.nodeType = nodeType;
    }
    public boolean getMarkedfordeletion() {
        return markedForDeletion;
    }

    public void setMarkedfordeletion(boolean markedForDeletion) {
        this.markedForDeletion = markedForDeletion;
    }
    public String getNodeid() {
        return nodeId;
    }

    public void setNodeid(String nodeId) {
        this.nodeId = nodeId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(LocalDate dateCreated) {
        this.dateCreated = dateCreated;
    }
    public int getSequence() {
        return sequence;
    }

    public void setSequence(int sequence) {
        this.sequence = sequence;
    }
    public String getParentnodetype() {
        return parentNodeType;
    }

    public void setParentnodetype(String parentNodeType) {
        this.parentNodeType = parentNodeType;
    }
    public String getParentnodeid() {
        return parentNodeId;
    }

    public void setParentnodeid(String parentNodeId) {
        this.parentNodeId = parentNodeId;
    }


}