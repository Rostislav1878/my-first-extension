import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
	console.log('Плагин "InsertTimestamp" активирован!');
	let disposable = vscode.commands.registerCommand('my-first-extension.insertTimestamp', () => {
		const editor = vscode.window.activeTextEditor;
		if (!editor) {
			return;
		}
		const now = new Date();

		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		const hours = String(now.getHours()).padStart(2, '0');
		const minutes = String(now.getMinutes()).padStart(2, '0');
		const seconds = String(now.getSeconds()).padStart(2, '0');
		const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
		editor.edit(editBuilder => {
			editBuilder.insert(editor.selection.active, formattedDate);
		});
		vscode.window.showInformationMessage(`Вставлено время: ${formattedDate}`);
	});
	context.subscriptions.push(disposable);
}
export function deactivate() {}
