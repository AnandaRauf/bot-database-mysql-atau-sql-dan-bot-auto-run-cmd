Public Class Form1
    Private Sub AutoRunCMDToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles AutoRunCMDToolStripMenuItem.Click
        Process.Start("Cmd.exe")
    End Sub
    Private Sub Autorunbtn_Click(sender As Object, e As EventArgs) Handles autorunbtn.Click
        Process.Start("Cmd.exe")
    End Sub


End Class
